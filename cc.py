#!/usr/bin/python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import sys
import os
import time
import random
import json
from StringIO import StringIO
import gzip

configFile = 'cc.conf'
config = SafeConfigParser()
config.read(configFile)

_server_host = 'http://api.chain-chronicle.net'

def login(in_account, in_password):
  setSession('INVALID')
  # takeover account data
  param = 'uuid=ando934daece-edc1-4435-9560-3313cbfe1c2f&account=' + in_account + '&pass=' + in_password
  apiRequest('/user/takeover', None, param)
  # generate session id
  login_path  = 'http://api.chain-chronicle.net/session/login?cnt=1412a53514d&timestamp=1379423405390'
  login_param = 'param=1FaQC07YMUGMAKXToXv4P5IiAeSejx5IsZw25%2bxr2XUFU5WLTAIx27KNz3Pl%2bRAHYtZWbYmRU4QeIa4DRTprk9clyWubbTWvWnnTifOmb7G6gub2AKN33eXnWRh6%2bpKNMpUH%2ftvY0aGNActhDArzJeuEcEKzoG5%2fC9yvJcMycH5T3jaT6uwrHb1TJOdUIs2O%2bzqnlqYyBkbpd0DbVn%2f9Yyqyf%2fY7IIajuUEMNpOYrloAWfFNttvtbTjw8WwjfQ4XXUNDmVKABaUnXbQtClMUESbAAByYt4aOUsDxb4ou3JFQGBr2QktFLxXzzO2VWUSxAUe7TU7F5FBkrrfTp%2fEHSzEIuFgy7DTGgABc8DpkvOv89MCCnarMZCp%2fK2CG1UA0SaECKsbS2qJXTT7imIGAlNkkm1M5QvMRgqF%2f3HFctFpn32dzt00NTRGJ%2fPYBNivi&nature=Lr9yCtV3xTt3h5NGMuXs4NraRfk%3d'
  response = apiLogin(login_path, login_param)
  login_path  = 'http://api.chain-chronicle.net/session/login?cnt=1412a5bbe53&timestamp=1379423957587'
  login_param = 'param=1FaQC07YMUGMAKXToXv4P5IiAeSejx5IsZw25%2bxr2XU8nwEYWyU9R0SJVlC276T1uY1W%2bPx7Cwlp9uPDTnbCLyrLbuMDUNEObPof6fUZixgWVtNfC2dhlxhEbGldBP41sfTKkcqs1PWM89m4ldOSwkR4d66Uym6K7fj4nmlZfn1r5JG5LRQbZ32yPaFtYcqSpEB5sjJtr3GTpnYyuN86p8q1hi4NBswOJ1mSNjhUnySjaWfTHg5%2bzi1yDG7lX00Lbu7qByyq4fxSVMHkG0KjxiwvWpGOdgg4ByYYnDcrR8GTMGkUPkEFkz5BzPNmQIH6GijHop5SC0RpvTsENE%2f%2fj6Sv0nboC%2bAs3AiVdxSEfJaO5phG52d9oE2hFBKeL0mOL6l3C2WtYzNilYM8P60iPq8u2a6ls2hTWSY2fp%2bwbaw5O963%2bS%2b1h%2fz60uYHLRdf&nature=WnS29LdBWj0NauSv5ikvnGzs45I%3d'
  response = apiLogin(login_path, login_param)
  setSession(response['login']['sid'])
  print 'account: %s' % setAccountPassword(in_password)

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
  curlCommand += '-H "AppVersion: 0.13" '
  
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
  response = json.loads(respDecord(os.popen(commandString).read()))
  if response['res'] != 0:
    print 'API error'
    print commandString
    print response
  return response

def respDecord(body):
  dd = [[0x52,0xd1,0x00,0x00,0x00,0x00,0x00,0x00], [0x25,0x03,0x36,0x84,0x16,0x13,0x00,0xe4,0x34,0x86]]
  num = min(0x40,len(body))
  for j in range(0, num, 1):
    if j < 8:
      body = body[:j] + chr(ord(body[j])^int(dd[0][j])) + body[j+1:]
    else:
      k = (j-8)%10
      body = body[:j] + chr(ord(body[j])^int(dd[1][k])) + body[j+1:]
  f = gzip.GzipFile(fileobj=StringIO(body))
  text = f.read()
  return text

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
  curlCommand += '-H "AppVersion: 0.13" '
  curlCommand += '-d "' + param + '" '
  response = None
  commandString = '%s "%s" 2>/dev/null' % (curlCommand, path)
  response = json.loads(respDecord(os.popen(commandString).read()))
  return response

def getPlayerStatus():
  return apiRequest('/user/all_data')

def printPlayerStatus(playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  for item in playerStatus['body'][7]['data']:
    if item['item_id'] == 10:
      playerGold = item['cnt']
    if item['item_id'] == 11:
      playerFP = item['cnt']
  playerStone = playerStatus['body'][10]['data']
  staMax  = playerStatus['body'][4]['data']['staminaMax']
  staTime = (playerStatus['body'][4]['data']['stmRefillTime'] - int(time.time())) / 60 
  staCur  = staMax if staTime < 0 else staMax - staTime / 8 - 1
  soulMax  = playerStatus['body'][4]['data']['powerMax']
  soulTime = (playerStatus['body'][4]['data']['pwrRefillTime'] - int(time.time())) / 60
  soulCur  = soulMax if soulTime < 0 else soulMax - soulTime / 30 - 1
  print 'Gold: %s / FP: %s / Stone: %s' % (playerGold, playerFP, playerStone)
  print 'exp: %s/%s (Lv %s)' % (playerStatus['body'][4]['data']['disp_exp'], playerStatus['body'][4]['data']['next_exp'], playerStatus['body'][4]['data']['lv'])
  print 'stamina: %s/%s (%s)' % (staCur, staMax, staTime)
  print 'soul: %s/%s (%s)' % (soulCur, soulMax, soulTime)

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
  
  # manually input situation
  if len(questIdList) == 1:
    questId = questIdList.pop()      
    questInfo  = parseMissionStatus(questId, statusInfo)
    return __battleQuest__(questInfo)
  
  questInfo = None
  while len(questIdList) > 0:
    questId = questIdList.pop()      
    questInfo  = parseMissionStatus(questId, statusInfo)
    if questInfo is None:
      continue
    if not checkQuestClear(questInfo):
      return __battleQuest__(questInfo)
    else:
      print '%s - cleared' % (questId)
  return questMain()

def questMain():
  statusInfo = getPlayerStatus()
  mainQuestList  = parseMainQuestList(statusInfo)
  mainQuestList.reverse()
  questInfo = mainQuestList[0]
  battleResponse = __battleQuest__(questInfo)
  if battleResponse is None:
    questId = questInfo['id']
    questType = questInfo['type']
    queryString = {}
    queryString.update({'qid' : questId})
    queryString.update({'type': questType})
    print apiRequest('/quest/treasure', queryString)
    return questId
  return None
    
def getFriendPendingList():
  resFriend = apiRequest('/friend/offered')
  return resFriend['body'][0]['data']['list']

def getFriendList():
  resFriend = apiRequest('/friend/list')
  return resFriend['body'][0]['data']['list']

def printFriendList(friendList):
  for friend in friendList:
    print "%s - [%2d] %s" % (friend['uid'], friend['lv'], friend['name'].encode("utf-8"))
    
def friendAccept(uid):
  queryString = {}
  queryString.update({'fid': uid})
  resFriend = apiRequest('/friend/accept', queryString)
  friendInfo = resFriend['body'][0]['data']['list'][0]
  print "%s - [%2d] %s" % (friend['uid'], friend['lv'], friend['name'].encode("utf-8"))
  
def friendRequest(uid):
  queryString = {}
  queryString.update({'fid' : uid})
  apiRequest('/friend/offer', queryString)
      
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
    
  elif sys.argv[1] == 'friend':
    try:
      subCommand = sys.argv[2]
      if subCommand == 'request':
        uid = sys.argv[3]
        friendRequest(uid)
      elif subCommand == 'accept':
        uid = sys.argv[3]
        friendAccept(uid)
      elif subCommand == 'pending':
        friendList = getFriendPendingList()
        printFriendList(friendList)
      elif subCommand == 'list':
        friendList = getFriendList()
        printFriendList(friendList)
      else:
        raise
    except:
      print('command for friend:')
      print('  list          : list current friends')
      print('  request <uid> : request <uid> for friend')
      print('  pending       : list who is asking to be your friend')
      print('  accept  <uid> : accept <uid> to be your friend')
      
  elif sys.argv[1] == 'boss':
    try:
      subCommand = sys.argv[2]
      if subCommand == 'list':
        bossList()
      elif subCommand == 'fight':
        bossId = sys.argv[3]
        bossFight(bossId)
      else:
        raise
    except:
      print('command for boss:')
      print('  list')
      print('  fight <bossid> : fight with boss')
      
  elif sys.argv[1] == 'genPass':
    password = sys.argv[2]
    setAccountPassword(password)
    print 'account: %s' % setAccountPassword(password)
  else:
    print 'command error - %s' % sys.argv[1]

if __name__ == "__main__":
  main()
