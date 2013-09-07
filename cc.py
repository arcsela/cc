#!/usr/bin/python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import sys
import os
import time
import random
import json

configFile = 'cc.conf'
config = SafeConfigParser()
config.read(configFile)

_server_host = 'http://api.chain-chronicle.net'

def loadSession():
  return config.get('session', 'sessionId')

def setSession(in_sessionId):
  config.set('session', 'sessionId', in_sessionId)
  fp = open(configFile, 'wb')
  config.write(fp)

def loadFriend():
  return config.get('player', 'friendId')

def loadQuestIdList():
  return json.loads(config.get('bot', 'questIdList'))

def loadSleepTime():
  return int(config.get('bot', 'sleeptime'))

def generateTimestamp():
  return hex(int(time.time() * 1000)).lstrip('0x')

def generateBattleTime():
  return str(random.uniform(2,5))[0:4]

def checkQuestClear(questInfo):
  if questInfo.has_key('treasure_idx'):
    if len(questInfo['treasure_idx']) == 4:
      return True
  return False

def apiRequest(path, in_queryString = None, in_param = None):
  curlCommand = 'curl --compressed '
  curlCommand += '-H "Host: api.chain-chronicle.net" '
  curlCommand += '-H "User-Agent: Chronicle/1.0.2 Rev/5662 (iPhone OS 6.0.2)" '
  curlCommand += '-H "Accept-Language: zh-tw" '
  curlCommand += '-H "Device: 6" '
  curlCommand += '-H "Accept: */*" '
  curlCommand += '-H "Platform: 1" '
  curlCommand += '-H "Content-Type: application/x-www-form-urlencoded" '
  curlCommand += '-H "Cookie: sid=' + loadSession() + '" '
  curlCommand += '-H "AppVersion: 0.11" '
  
  param = ''
  if in_param:
    param = in_param + '&'
  param += 'nature=qZXnbieHGRwPTaM4vAYfQi6WY3I%3d'
  curlCommand += '-d "' + param + '" '
 
  queryString = '?'
  queryString += 'cnt=' + generateTimestamp()
  if in_queryString:
    for key in in_queryString:
      queryString += '&' + key + '=' + str(in_queryString[key])
    
  response = None
  commandString = '%s "%s%s%s" 2>/dev/null' % (curlCommand, _server_host, path, queryString)
  response = json.loads(os.popen(commandString).read())
  if response['res'] != 0:
    print 'API error'
    print commandString
    print response
  return response

def getPlayerStatus():
  return apiRequest('/user/all_data')

def printPlayerStatus(playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  print 'exp: %s/%s' % (playerStatus['body'][4]['data']['disp_exp'], playerStatus['body'][4]['data']['next_exp'])
  print 'stamina: %s/%s' % (playerStatus['body'][4]['data']['staminaMax'] - (playerStatus['body'][4]['data']['stmRefillTime'] - int(time.time())) / 60 / 8, playerStatus['body'][4]['data']['staminaMax'])

def printPlayerInfo(playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  print 'account id: %s' % (playerStatus['body'][4]['data']['open_id'])
  print 'fid: %s' % (playerStatus['body'][4]['data']['uid'])

def parseMissionStatus(questid, playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  for quest in playerStatus['body'][3]['data']:
    if quest['id'] == int(questid):
      return quest
  return None

def printMissionStatus(questid):
  missionStatus = parseMissionStatus(questid)
  if missionStatus is None:
    print 'quest not found: %s' % (questid)
    return None
  print 'quest id: %s' % (missionStatus['id'])
  print 'type  id: %s' % (missionStatus['type'])
  if missionStatus.has_key('treasure_idx'):
    treasureCount = len(missionStatus['treasure_idx'])
  else:
    treasureCount = 0
  print 'treasure: %s/%s' % (treasureCount, '4')

def login():
  config.set('session', 'sessionId', 'INVALID')
  fp = open(configFile, 'wb')
  config.write(fp)
  config.read(configFile)
  return apiRequest('/session/login', None, 'param=%7b%22App%22%3a%7b%22Ver%22%3a%220.11%22%2c%22Rev%22%3a%225662%22%7d%2c%22Device%22%3a%7b%22DeviceModel%22%3a%22iPhone5%2c2%22%2c%22Processor%22%3a%22armv7s%22%2c%22Graphics%22%3a%22PowerVR+SGX+543%22%2c%22OSVer%22%3a%22iPhone+OS+6.0.2%22%2c%22UUID%22%3a%22FEEE070C-304D-4E5D-9B65-9FA794A39ADB%22%2c%22RAM%22%3a1015%2c%22VRAM%22%3a256%2c%22OS%22%3a%221%22%2c%22Generation%22%3a%22iPhone5%22%2c%22Token%22%3a%227DA6BFE18BE8E5BD7136CF88761F75E3A95EE542F027A0F77C0882660020DF1B%22%7d%7d')
  
def battleInit(typeId, questId):
  queryString = {}
  queryString.update({'qid' : questId})
  queryString.update({'type': typeId})
  queryString.update({'fid' : loadFriend()})
  return apiRequest('/quest/entry', queryString)
  
def questWin(questId):
  queryString = {}
  queryString.update({'qid' : questId})
  queryString.update({'res' : '1'})
  queryString.update({'time': generateBattleTime()})
  queryString.update({'d': '1'})
  queryString.update({'s': '1'})
  return apiRequest('/quest/result', queryString)

def printBattleResult(in_battleResult):
  #print in_battleResult
  if in_battleResult['res'] == 0:
    if in_battleResult.has_key('earns'):
      print 'EXP: %s / GOLD: %s (bonus %s)' % (in_battleResult['earns']['exp'], in_battleResult['earns']['gold'], in_battleResult['earns']['bonus_gold'])
      for item in in_battleResult['earns']['treasure']:
        print 'Treasure: %s - %s x %s' % (item['type'], item['id'], item['val'])
    if in_battleResult.has_key('quest_reward'):
      print 'QUEST COMPLETED REWARD!!!'
      print in_battleResult['quest_reward']
  return in_battleResult

def __battleQuest__(questInfo):
  questType = questInfo['type']
  questId   = questInfo['id']
  resBattleInit = battleInit(questType, questId)
  if resBattleInit['res'] == 0:
    print 'battle inital completed'
    time.sleep(30)
    print 'battle end - %s' % (questId)
    resBattleResult = questWin(questId)
    printBattleResult(resBattleResult)
    return True
  return False

def quest(questIdList):
  # convert battleId into array
  if type(questIdList) is str:
    questIdList = [questIdList]
  questIdList.reverse()
  statusInfo = getPlayerStatus()
  
  while len(questIdList) > 0:
    questId = questIdList.pop()
    questInfo  = parseMissionStatus(questId, statusInfo)
    if not checkQuestClear(questInfo):
      return __battleQuest__(questInfo)
  # battle with last entry if no match
  return __battleQuest__(questInfo)
      
def bot_mode():
  sleepTime = loadSleepTime()
  questIdList = loadQuestIdList()
  while True:
    currentSleepTime = 0
    quest(questIdList)
    while currentSleepTime < sleepTime:
      playerStatus = getPlayerStatus()
      printPlayerStatus(playerStatus)
      if playerStatus['body'][4]['data']['stmRefillTime'] < int(time.time()):
        break
      print 'sleep: %s/%s' % (currentSleepTime, sleepTime)
      time.sleep(60)
      currentSleepTime += 1

def main():
  if sys.argv[1] == 'login':
    pass
  elif sys.argv[1] == 'session':
    newSession = sys.argv[2]
    setSession(newSession)
  elif sys.argv[1] == 'bot':
    bot_mode()
  elif sys.argv[1] == 'quest':
    questId = sys.argv[2]
    quest(questId)
  elif sys.argv[1] == 'questWin':
    questId = sys.argv[2]
    questWin(questID)
  elif sys.argv[1] == 'questInfo':
    questId = sys.argv[2]
    printMissionStatus(questId)
  elif sys.argv[1] == 'playerInfo':
    printPlayerInfo()
    printPlayerStatus()
  else:
    print 'command error - %s' % sys.argv[1]

if __name__ == "__main__":
  main()