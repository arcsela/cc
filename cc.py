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
import gacha

configFile = 'cc.conf'
config = SafeConfigParser()
config.read(configFile)

_server_host = 'http://api.chain-chronicle.net'

RECOVER_TIME_STA  = 8
RECOVER_TIME_SOUL = 30

def login(in_account, in_password):
  setSession('INVALID')
  # takeover account data
  param = 'uuid=ando934daece-edc1-4435-9560-3313cbfe1c2f&account=' + in_account + '&pass=' + in_password
  response = apiRequest('/user/takeover', None, param)
  if response['res'] != 0:
    print 'takeover err'
    exit()
  # generate session id
  login_path  = 'http://api.chain-chronicle.net/session/login?cnt=1412a53514d&timestamp=1379423405390'
  login_param = 'param=1FaQC07YMUGMAKXToXv4P5IiAeSejx5IsZw25%2bxr2XUFU5WLTAIx27KNz3Pl%2bRAHYtZWbYmRU4QeIa4DRTprk9clyWubbTWvWnnTifOmb7G6gub2AKN33eXnWRh6%2bpKNMpUH%2ftvY0aGNActhDArzJeuEcEKzoG5%2fC9yvJcMycH5T3jaT6uwrHb1TJOdUIs2O%2bzqnlqYyBkbpd0DbVn%2f9Yyqyf%2fY7IIajuUEMNpOYrloAWfFNttvtbTjw8WwjfQ4XXUNDmVKABaUnXbQtClMUESbAAByYt4aOUsDxb4ou3JFQGBr2QktFLxXzzO2VWUSxAUe7TU7F5FBkrrfTp%2fEHSzEIuFgy7DTGgABc8DpkvOv89MCCnarMZCp%2fK2CG1UA0SaECKsbS2qJXTT7imIGAlNkkm1M5QvMRgqF%2f3HFctFpn32dzt00NTRGJ%2fPYBNivi&nature=Lr9yCtV3xTt3h5NGMuXs4NraRfk%3d'
  response = apiLogin(login_path, login_param)
  login_path  = 'http://api.chain-chronicle.net/session/login?cnt=1412a5bbe53&timestamp=1379423957587'
  login_param = 'param=1FaQC07YMUGMAKXToXv4P5IiAeSejx5IsZw25%2bxr2XU8nwEYWyU9R0SJVlC276T1uY1W%2bPx7Cwlp9uPDTnbCLyrLbuMDUNEObPof6fUZixgWVtNfC2dhlxhEbGldBP41sfTKkcqs1PWM89m4ldOSwkR4d66Uym6K7fj4nmlZfn1r5JG5LRQbZ32yPaFtYcqSpEB5sjJtr3GTpnYyuN86p8q1hi4NBswOJ1mSNjhUnySjaWfTHg5%2bzi1yDG7lX00Lbu7qByyq4fxSVMHkG0KjxiwvWpGOdgg4ByYYnDcrR8GTMGkUPkEFkz5BzPNmQIH6GijHop5SC0RpvTsENE%2f%2fj6Sv0nboC%2bAs3AiVdxSEfJaO5phG52d9oE2hFBKeL0mOL6l3C2WtYzNilYM8P60iPq8u2a6ls2hTWSY2fp%2bwbaw5O963%2bS%2b1h%2fz60uYHLRdf&nature=WnS29LdBWj0NauSv5ikvnGzs45I%3d'
  response = apiLogin(login_path, login_param)
  setSession(response['login']['sid'])
  print 'account: %s' % setAccountPassword(in_password)

def login2(header, body):
  #setSession('INVALID')
  response = apiLogin(header, body)
  setSession(response['login']['sid'])
  print 'account: %s' % setAccountPassword('1234qwer')

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
  
def loadBossFight():
  cfgBossFight = config.get('bot', 'bossFight')
  if int(cfgBossFight) == 0:
    return False
  else:
    return True

def loadFriend():
  return config.get('player', 'friendId')

def loadQuestIdList():
  return json.loads(config.get('bot', 'questIdList'))

def loadQuestFinal():
  return config.get('bot', 'questidfinal')

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
  playerGold = 0
  playerFP = 0
  playerRing = 0
  for item in playerStatus['body'][7]['data']:
    if item['item_id'] == 10:
      playerGold = item['cnt']
    if item['item_id'] == 11:
      playerFP = item['cnt']
    if item['item_id'] == 13:
      playerRing = item['cnt']
  playerStone = playerStatus['body'][10]['data']
  staMax  = playerStatus['body'][4]['data']['staminaMax']
  staTime = (playerStatus['body'][4]['data']['stmRefillTime'] - int(time.time())) / 60 
  staCur  = staMax if staTime < 0 else staMax - staTime / RECOVER_TIME_STA - 1
  soulMax  = playerStatus['body'][4]['data']['powerMax']
  soulTime = (playerStatus['body'][4]['data']['pwrRefillTime'] - int(time.time())) / 60
  soulCur  = soulMax if soulTime < 0 else soulMax - soulTime / RECOVER_TIME_SOUL - 1
#  print 'Gold: %s / FP: %s / Stone: %s' % (playerGold, playerFP, playerStone)
#  print 'exp: %s/%s (Lv %s)' % (playerStatus['body'][4]['data']['disp_exp'], playerStatus['body'][4]['data']['next_exp'], playerStatus['body'][4]['data']['lv'])
  print 'RANK%s, Exp: %s/%s' % (playerStatus['body'][4]['data']['lv'], playerStatus['body'][4]['data']['disp_exp'], playerStatus['body'][4]['data']['next_exp'])
  for form in playerStatus['body'][4]['data']['mainForm']:
    print cardInfo(form,playerStatus)
  for form in playerStatus['body'][4]['data']['subForm']:
    print cardInfo(form,playerStatus)
  print 'Stone: %s , Gold: %s , AC: %s, Ring: %s, ' % (playerStone, playerGold, playerFP, playerRing) + 'Card: %s/%s' % (len(playerStatus['body'][5]['data']), playerStatus['body'][4]['data']['cardMax']) 
  print 'AP: %s/%s (%s)' % (staCur, staMax, staTime % RECOVER_TIME_STA)
  print 'Soul: %s/%s (%s)' % (soulCur, soulMax, soulTime % RECOVER_TIME_SOUL)

def printPlayerInfo(playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  Aid = str(playerStatus['body'][4]['data']['open_id'])
  print 'AID: %s,%s,%s' % (Aid[:3], Aid[3:6], Aid[6:])
  print 'FID: %s' % (playerStatus['body'][4]['data']['uid'])

def cardInfo(idx, playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  for item in playerStatus['body'][5]['data']:
    if item['idx'] == int(idx):
      if item['type'] == 0:
        return 'Lv: %2s/%2s, ' % (item['lv'],item['maxlv']) + 'EXP: %5s/%5s, ' % (item['disp_exp'], item['next_exp']) + 'HP:%5s, ATK:%5s, ' % (item['hp'], item['atk']) + 'WP:%2s/%2s/%2s, ' % (item['weaponAttack'], item['weaponCritical'], item['weaponGuard']) + 'No.%05d ' % int(item['id']) + '%s' % gacha.i2n(item['id'],item['type']) + '+%s' % item['limit_break']
        
      else:
        return item


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

def printMissionList(typeid = None, data = 3):
  playerStatus = getPlayerStatus()
  for quest in playerStatus['body'][data]['data']:
    if not typeid or quest['type'] == int(typeid):
      if data == 3:
        if quest.has_key('treasure_idx'):
          print '%s - %s/4' % (quest['id'], len(quest['treasure_idx']))
        else:
          print '%s - 0/4' % (quest['id'])
      else:
        print '%s' % (quest['id'])

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
        print 'Treasure:  %s' %  gacha.i2n(item['id'], item['type'], item['val'])
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
  playerStatus = getPlayerStatus()
  
  # manually input situation
  if len(questIdList) == 1:
    questId = questIdList.pop()      
    questInfo  = parseMissionStatus(questId, playerStatus)
    return __battleQuest__(questInfo)
  
  questInfo = None
  while len(questIdList) > 0:
    questId = questIdList.pop()      
    questInfo  = parseMissionStatus(questId, playerStatus)
    if questInfo is None:
      continue
    if not checkQuestClear(questInfo):
      return __battleQuest__(questInfo)
    else:
      print '%s - cleared' % (questId)
  questId = loadQuestFinal()
  questInfo = parseMissionStatus(questId, playerStatus)
  if questInfo is not None:
    __battleQuest__(questInfo)
  elif parseQuestSub(playerStatus) is not None:
    subQuestInfo = parseQuestSub(playerStatus)
    __battleQuest__(subQuestInfo)
  else:
    return questMain()
  
def parseQuestSub(playerStatus = None,questid = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  for dataGroup in playerStatus['body']:
    if dataGroup['type'] == 6:
      for quest in dataGroup['data']:
        if questid is None:
          if quest['stepNow'] >= 0 and not quest.has_key('treasure_idx'):
            return quest
        else:
          if quest['id'] == int(questid):
            return quest
  return None

def questMain(playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  mainQuestList  = parseMainQuestList(playerStatus)
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
      
def bossList():
  resBossList = apiRequest('/raid/list')
  for body in resBossList['body']:
    if body['type'] == 10:
      return body['data']
    
def printBossList(resBossList):
  for boss in resBossList:
    bossId = boss['boss_id']
    bossTime = (boss['validtime'] - int(time.time())) / 60
    bossLv = boss['boss_param']['lv']
    bossHp = boss['boss_param']['hp']
    bossHpMax = boss['boss_param']['hpMax']
    bossOwner = boss['discoverer_name']
    if bossTime > 0 and bossHp > 0:
      print '%9s - %3d minutes - Lv:%2d (%s/%s) - %s' % (bossId, bossTime, bossLv, bossHp, bossHpMax, bossOwner.encode('utf-8'))
    else:
      bossCollect(bossId)

def bossInfo(resBossList, bossId = None, myId = None):
  for boss in resBossList:
    if (bossId is None) and (myId is None):
      # return first boss if nothing is provided
      return boss
    elif (myId is not None):
      # return only my own boss if myId is provided
      if str(boss['discoverer']) == str(myId):
        return boss
      else:
        continue
    elif (str(boss['boss_id']) == str(bossId)):
      return boss
  return None
    
def bossFight(resBossInfo, currentSleepTime = None, sleepTime = None):
  if resBossInfo is None:
    return None
  bossId = resBossInfo['boss_id']
  bossHp = resBossInfo['boss_param']['hp']
  resInit = bossFightInit(bossId)
  if resInit['res'] != 0:
    return None
  time.sleep(60)
  bossFightResult(bossId, bossHp)
  bossCollect(bossId)

def bossFightInit(bossId):
  print 'fight with boss: %s' % (bossId)
  queryString = {}
  queryString.update({'bid' : bossId})
  queryString.update({'use' : '1'})
  queryString.update({'fid' : loadFriend()})
  return apiRequest('/raid/entry', queryString)
  
def bossFightResult(bossId, bossDamage):
  print 'fight end: %s' % (bossId)
  queryString = {}
  queryString.update({'bid' : bossId})
  queryString.update({'res' : '1'})
  queryString.update({'damage' : bossDamage})
  queryString.update({'t' : '8'})
  resFightResult = apiRequest('/raid/result', queryString)
  printBattleResult( resFightResult )
  
def bossCollect(bossId):
  print 'collect: %s' % (bossId)
  queryString = {}
  queryString.update({'bid' : bossId})
  apiRequest('/raid/record', queryString)  

def bot_mode():
  sleepTime = loadSleepTime()
  while True:
    playerStatus = getPlayerStatus()
    printPlayerStatus(playerStatus)
    currentSleepTime = 0
    questIdList = loadQuestIdList()
    quest(questIdList)
    while currentSleepTime < sleepTime:
      playerStatus = getPlayerStatus()
      printPlayerStatus(playerStatus)
      if playerStatus['body'][4]['data']['stmRefillTime'] < int(time.time()):
        break
      staMax  = playerStatus['body'][4]['data']['staminaMax']
      staTime = (playerStatus['body'][4]['data']['stmRefillTime'] - int(time.time())) / 60
      staCur  = staMax if staTime < 0 else staMax - staTime / RECOVER_TIME_STA - 1
      soulMax  = playerStatus['body'][4]['data']['powerMax']
      soulTime = (playerStatus['body'][4]['data']['pwrRefillTime'] - int(time.time())) / 60
      soulCur  = soulMax if soulTime < 0 else soulMax - soulTime / RECOVER_TIME_SOUL - 1
      if loadBossFight():
        printBossList(bossList())
        resBossList = bossList()
        if soulCur > 0:
          resBossInfo = bossInfo(resBossList, None, playerStatus['body'][4]['data']['uid'])
          if resBossInfo is not None:
            bossFight(resBossInfo, currentSleepTime, sleepTime)
            break
          elif staCur >= 4:
            quest('220103')
          
      print 'sleep: %s/%s' % (currentSleepTime, sleepTime)
      time.sleep(60)
      currentSleepTime += 1

def printCard(type,playerStatus = None):
  if playerStatus is None:
    playerStatus = getPlayerStatus()
  for item in playerStatus['body'][5]['data']:
    if type == -1:
      print '[%s] ' % item['idx'] + 'No.%05d %s ' % (int(item['id']), gacha.i2n(item['id'],item['type']))
    elif type == 0 and item['type'] == 0:
      print '[%s] ' % item['idx'] + '%s' % cardInfo(item['idx'],playerStatus)
    elif type == 1 and item['type'] == 1:
      print '[%s] ' % item['idx'] + 'No.%05d %s ' % (int(item['id']), gacha.i2n(item['id'],item['type']))
    elif type > 1 and item['type'] > 1:
      print '[%s] ' % item['idx'] + 'No.%05d %s ' % (int(item['id']), gacha.i2n(item['id'],item['type']))

def printPresentList(presentList = None):
  if presentList is None:
    presentList = getPresentList()
  presentIdList = presentList['body'][0]['data']
  for present in presentIdList:
    #print '[%s]' % present['idx'] + ' %s - %s x %s' % (present['data']['type'], gacha.i2n(int(present['data']['id'])), present['data']['val'])
    print '[%s]' % present['idx'] + ' %s ' % gacha.i2n(present['data']['id'],present['data']['type'],present['data']['val'])

def getPresentList():
  return apiRequest('/present/list')

def sellCard( idx,playerStatus = None ):
  #no playerStatus no check locked
  queryString = {}
  queryString.update({'c' : idx})
  if playerStatus is None:
    response = apiRequest('/card/sell', queryString)
    if response['res'] == 0:
      print '%s is selled.' % idx 
    return
  for item in playerStatus['body'][5]['data']:
    if item['idx'] == int(idx):
      if item.get('locked', False) == True:
        print '%s is lock.' % idx 
        return
      else:
        response = apiRequest('/card/sell', queryString)
        if response['res'] == 0:
          print '%s is selled.' % idx 
        return
  print 'no match idx(%s).' % idx

def autoSellBox():
  presentIdList = apiRequest('/present/list?')['body'][0]['data']
  for present in presentIdList:
    if( gacha.i2as(present['data']['id'],present['data']['type']) ):
      print '\033[1;31m[%s]' % present['idx'] + ' %s \033[m' % gacha.i2n(present['data']['id'],present['data']['type'],present['data']['val'])
      print 'sell after 2 seconds...'
      time.sleep(2)
      queryString = {}
      queryString.update({'p' : present['idx']})
      response = apiRequest('/present/recv', queryString)
      sellCard(response['body'][0]['data'][0]['idx'])
    else:
      print '\033[1;30m[%s]' % present['idx'] + ' %s \033[m' % gacha.i2n(present['data']['id'],present['data']['type'],present['data']['val'])
    '''
    if( present['data']['type'] == 'card' ):
      queryString = {}
      queryString.update({'p' : present['idx']})
      response = apiRequest('/present/recv', queryString)
      #print '[%s] ' % response['body'][0]['data'][0]['idx'] + 'No.%05d ' % int(response['body'][0]['data'][0]['id']) + '%s' % cardInfo(response['body'][0]['data'][0]['idx'])
      star = getCardStar(response['body'][0]['data'][0]['idx'])
      if star < 3:
        print '\033[1;31m[%s]' % present['idx'] + ' %s \033[m' % gacha.i2n(present['data']['id'],present['data']['type'],present['data']['val'])
        #print 'this card is %sS, to sell.' % star
        sellCard(response['body'][0]['data'][0]['idx'])
      else:
        print '\033[1;33m[%s]' % present['idx'] + ' %s \033[m' % gacha.i2n(present['data']['id'],present['data']['type'],present['data']['val'])        
        #print 'this card is %sS.' % star
      
    elif( present['data']['type'] == 'chara_rf'):
      print '\033[1;31m[%s]' % present['idx'] + ' %s \033[m' % gacha.i2n(present['data']['id'],present['data']['type'],present['data']['val'])
      star = (int(present['data']['id'])-90000)/5+1
      if star < 2:
        queryString = {}
        queryString.update({'p' : present['idx']})
        response = apiRequest('/present/recv', queryString)
      #  print 'this card is %sS, to sell.' % star
        sellCard(response['body'][0]['data'][0]['idx'])
      #else:
      #  print 'this card is %sS.' % star
    else:
      #print present['idx']
      print '\033[1;30m[%s]' % present['idx'] + ' %s \033[m' % gacha.i2n(present['data']['id'],present['data']['type'],present['data']['val'])
    #print present
      '''
def autoSellCard():
  resPlayerStatus = getPlayerStatus()
  for item in resPlayerStatus['body'][5]['data']:
    if( gacha.i2as(item['id'],item['type']) ):
      print '\033[1;31m[%s]' % item['idx'] + ' %s \033[m' % gacha.i2n(item['id'],item['type'])
      print 'sell after 2 seconds...'
      time.sleep(2)
      sellCard(item['idx'], resPlayerStatus)
    else:
      print '\033[1;30m[%s]' % item['idx'] + ' %s \033[m' % gacha.i2n(item['id'],item['type'])

    '''
    if( item['type'] == 0 ):
      star = getCardStar(item['idx'])
      if star < 3:
        print '\033[1;31m[%s]' % item['idx'] + ' %s \033[m' % gacha.i2n(item['id'],item['type'])
        sellCard(item['idx'])
      else:
        print '\033[1;30m[%s]' % item['idx'] + ' %s \033[m' % gacha.i2n(item['id'],item['type'])
        
    elif( item['type'] == 3 ):
      star = (int(item['id'])-90000)/5+1
      if star < 2:
        print '\033[1;31m[%s]' % item['idx'] + ' %s \033[m' % gacha.i2n(item['id'],item['type'])
        sellCard(item['idx'])
      else:
        print '\033[1;30m[%s]' % item['idx'] + ' %s \033[m' % gacha.i2n(item['id'],item['type'])
    else:
      print '\033[1;30m[%s]' % item['idx'] + ' %s \033[m' % gacha.i2n(item['id'],item['type'])
    '''


def main():
  sys.path.append(os.getcwd())
  if sys.argv[1] == 'login':
    if os.path.exists('login_http.py'):
      import login_http
      login2(login_http.header, login_http.body)
    elif len(sys.argv) >= 4:
      login(sys.argv[2], sys.argv[3])
    else:
      print 'login <id> <pw>'
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
  elif sys.argv[1] == 'questSubList':
    if len(sys.argv) == 3:
      printMissionList(sys.argv[2],2)
    else:
      printMissionList(None,2)
  elif sys.argv[1] == 'quest':
    questId = sys.argv[2]
    quest(questId)
  elif sys.argv[1] == 'questSub':
    playerStatus = getPlayerStatus()
    if len(sys.argv) == 3:
      questId = sys.argv[2]
      questInfo = parseQuestSub(playerStatus,questId)
      __battleQuest__(questInfo)
    else:
      questInfo = parseQuestSub(playerStatus)
      __battleQuest__(questInfo)
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
      printPlayerInfo()
      print('command for friend:')
      print('  list          : list current friends')
      print('  request <uid> : request <uid> for friend')
      print('  pending       : list who is asking to be your friend')
      print('  accept  <uid> : accept <uid> to be your friend')
      
  elif sys.argv[1] == 'boss':
    try:
      subCommand = sys.argv[2]
      if subCommand == 'list':
        res = bossList()
        printBossList(res)
      elif subCommand == 'fight':
        bossId = sys.argv[3]
        res = bossList()
        res = bossInfo(res, bossId)
        bossFight(res)
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
    
  elif sys.argv[1] == 'recv':
    y = len(sys.argv) - 2
    for x in range(0, y, 1):
      idx = sys.argv[x+2]
      queryString = {}
      queryString.update({'p' : idx})
      response = apiRequest('/present/recv', queryString)
      if response['res'] == 0:
        item = response['body'][0]['data']
        print '[%s] ' % item[0]['idx'] + 'No.%05d ' % int(item[0]['id']) + '%s' % cardInfo(item[0]['idx']) 

  elif sys.argv[1] == 'autosell':
    try:
      subCommand = sys.argv[2]
      if subCommand == 'box':
        autoSellBox()
      elif subCommand == 'card':
        autoSellCard()
      else:
        raise
    except:
      print('command for autosell: card, box')

  elif sys.argv[1] == 'sell':
    y = len(sys.argv) - 2
    for x in range(0, y, 1):
      idx = sys.argv[x+2]
      resPlayerStatus = getPlayerStatus()
      sellCard(idx,resPlayerStatus)

  elif sys.argv[1] == 'acdraw':
    num = sys.argv[2]
    queryString = {}
    queryString.update({'t' : 0})
    queryString.update({'c' : num})
    response = apiRequest('/gacha', queryString)
    if response['res'] == 0:
      print response
 
  elif sys.argv[1] == 'card':
    try:
      subCommand = sys.argv[2]
      if subCommand == 'rf':
        printCard(2)
      elif subCommand == 'wp':
        printCard(1)
      elif subCommand == 'ch':
        printCard(0)
      elif subCommand == 'all':
        printCard(-1)
      else:
        raise
    except:
      print('command for card: ch, rf, wp, all')


  elif sys.argv[1] == 'box':
    printPresentList()
    
  elif sys.argv[1] == 'recovery_ap':
    queryString = {}
    queryString.update({'type' : 1})
    response = apiRequest('/user/recover_ap', queryString)

  elif sys.argv[1] == 'evdraw':
    resPlayerStatus = getPlayerStatus()
    eventPoint = 0
    for item in resPlayerStatus['body'][7]['data']:
      if item['item_id'] == 12:
        eventPoint = item['cnt']
        break
    print 'event point: %s' % (eventPoint)
    drawTotal = eventPoint / 200
    while drawTotal > 0:
      time.sleep(5)
      drawCnt = 10 if drawTotal >= 10 else drawTotal
      drawTotal -= drawCnt
      if drawCnt > 0:
        queryString = {}
        queryString.update({'t':3})
        queryString.update({'c':drawCnt})
        response = apiRequest('/gacha', queryString)
        for card in response['present_card_list']:
          print 'card id: %s' % (gacha.i2n(int(card['cid'])))
           
  else:
    print 'command error - %s' % sys.argv[1]

if __name__ == "__main__":
  main()
