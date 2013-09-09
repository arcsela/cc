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

def login(in_account, in_password):
  setSession('INVALID')
  # takeover account data
  param = 'uuid=ando74c139c3-e340-4c01-8ed2-afe91c7db197&account=' + in_account + '&pass=' + in_password
  apiRequest('/user/takeover', None, param)
  # generate session id
  login_path  = 'http://api.chain-chronicle.net/session/login?cnt=140fe298a8e'
  login_param = 'param=%7b%22App%22%3a%7b%22Ver%22%3a%220.11%22%2c%22Rev%22%3a%225662%22%7d%2c%22Device%22%3a%7b%22DeviceModel%22%3a%22asus+ME371MG%22%2c%22Processor%22%3a%22ARMv7+VFPv3%22%2c%22Graphics%22%3a%22PowerVR+SGX+540%22%2c%22OSVer%22%3a%22Android+OS+4.1.2+%2f+API-16+(JZO54K%2fTW_epad-V3.2.4-20130712)%22%2c%22UUID%22%3a%22ando74c139c3-e340-4c01-8ed2-afe91c7db197%22%2c%22RAM%22%3a967%2c%22VRAM%22%3a60%2c%22OS%22%3a%222%22%2c%22Token%22%3a%22%22%7d%7d&nature=tfsTbCiLB9O7X43t0Me%2bXzbw8og%3d'
  apiLogin(login_path, login_param)
  login_path  = 'http://api.chain-chronicle.net/session/login?cnt=140fe2bfbd0'
  login_param = 'param=%7b%22App%22%3a%7b%22Ver%22%3a%220.11%22%2c%22Rev%22%3a%225662%22%7d%2c%22Device%22%3a%7b%22DeviceModel%22%3a%22asus+ME371MG%22%2c%22Processor%22%3a%22ARMv7+VFPv3%22%2c%22Graphics%22%3a%22PowerVR+SGX+540%22%2c%22OSVer%22%3a%22Android+OS+4.1.2+%2f+API-16+(JZO54K%2fTW_epad-V3.2.4-20130712)%22%2c%22UUID%22%3a%22ando74c139c3-e340-4c01-8ed2-afe91c7db197%22%2c%22RAM%22%3a967%2c%22VRAM%22%3a60%2c%22OS%22%3a%222%22%2c%22Token%22%3a%22%22%7d%7d&nature=uksU%2bngwYzywumNK0LDjTSXd6fQ%3d'
  apiLogin(login_path, login_param)
  # genPass
  setAccountPassword(in_password)

def setAccountPassword(password):
  resAccount = apiRequest('/user/get_account')
  queryString = {}
  queryString.update({'pass' : password})
  apiRequest('/user/set_password', queryString)
  return resAccount['account']

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

def apiLogin(path, param):
  curlCommand = 'curl --compressed '
  curlCommand += '-H "Host: api.chain-chronicle.net" '
  curlCommand += '-H "User-Agent: Chronicle/1.0.2 Rev/5662 (iPhone OS 6.0.2)" '
  curlCommand += '-H "Accept-Language: zh-tw" '
  curlCommand += '-H "Device: 6" '
  curlCommand += '-H "Accept: */*" '
  curlCommand += '-H "Platform: 1" '
  curlCommand += '-H "Content-Type: application/x-www-form-urlencoded" '
  curlCommand += '-H "Cookie: sid=INVALID" '
  curlCommand += '-H "AppVersion: 0.11" '
  curlCommand += '-d "' + param + '" '
  response = None
  commandString = '%s "%s" 2>/dev/null' % (curlCommand, path)
  response = json.loads(os.popen(commandString).read())
  setSession(response['login']['sid'])

def getPlayerStatus():
  return apiRequest('/user/all_data')

def printPlayerStatus(playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  print 'exp: %s/%s (Lv %s)' % (playerStatus['body'][4]['data']['disp_exp'], playerStatus['body'][4]['data']['next_exp'], playerStatus['body'][4]['data']['lv'])
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

def parseMainQuestList(playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  return playerStatus['body'][1]['data']

def printMissionList(typeid = None):
  playerStatus = getPlayerStatus()
  for quest in playerStatus['body'][3]['data']:
    if not typeid or quest['type'] == int(typeid):
      if quest.has_key('treasure_idx'):
        print '%s - %s/4' % (quest['id'], len(quest['treasure_idx']))
      else:
        print '%s - 0/4' % (quest['id'])

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
    return questId
  return None

def quest(questIdList):
  # convert battleId into array
  if type(questIdList) is str:
    questIdList = [questIdList]
  questIdList.reverse()
  statusInfo = getPlayerStatus()
  
  questInfo = None
  while len(questIdList) > 0:
    questId = questIdList.pop()      
    questInfo  = parseMissionStatus(questId, statusInfo)
    if questInfo is None:
      continue
    if not checkQuestClear(questInfo):
      return __battleQuest__(questInfo)
    elif len(questIdList) == 0:
      return __battleQuest__(questInfo)
    else:
      print '%s - cleared' % (questId)
  print 'no matched quest'
  return None

def questMain():
  statusInfo = getPlayerStatus()
  mainQuestList  = parseMainQuestList(statusInfo)
  mainQuestList.reverse()
  questInfo = mainQuestList[0]
  battleResponse = __battleQuest__(questInfo)
  if battleResponse is None:
    questId = questInfo['id']
    queryString = {}
    queryString.update({'qid' : questId})
    queryString.update({'type': '5'})
    print apiRequest('/quest/treasure', queryString)
      
def bot_mode():
  sleepTime = loadSleepTime()
  while True:
    currentSleepTime = 0
    questIdList = loadQuestIdList()
    quest(questIdList)
    while currentSleepTime < sleepTime:
      playerStatus = getPlayerStatus()
      printPlayerStatus(playerStatus)
      if playerStatus['body'][4]['data']['stmRefillTime'] < int(time.time()):
        break
      print 'sleep: %s/%s\n' % (currentSleepTime, sleepTime)
      time.sleep(60)
      currentSleepTime += 1

def main():
  if sys.argv[1] == 'login':
    login(sys.argv[2], sys.argv[3])
  elif sys.argv[1] == 'session':
    newSession = sys.argv[2]
    setSession(newSession)
  elif sys.argv[1] == 'bot':
    bot_mode()
  elif sys.argv[1] == 'questList':
    if len(sys.argv) == 3:
      printMissionList(sys.argv[2])
    else:
      printMissionList()
  elif sys.argv[1] == 'quest':
    questId = sys.argv[2]
    quest(questId)
  elif sys.argv[1] == 'questMain':
    questMain()
  elif sys.argv[1] == 'questWin':
    questId = sys.argv[2]
    resBattleResult = questWin(questId)
    printBattleResult(resBattleResult)
  elif sys.argv[1] == 'questInfo':
    questId = sys.argv[2]
    printMissionStatus(questId)
  elif sys.argv[1] == 'playerInfo':
    printPlayerInfo()
    printPlayerStatus()
  elif sys.argv[1] == 'genPass':
    password = sys.argv[2]
    resAccount = apiRequest('/user/get_account')
    queryString = {}
    queryString.update({'pass' : password})
    apiRequest('/user/set_password', queryString)
    print 'account: %s' % (resAccount['account'])
  else:
    print 'command error - %s' % sys.argv[1]

if __name__ == "__main__":
  main()