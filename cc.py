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

def loadFriend():
  return config.get('player', 'friendId')

def loadBattleId():
  return config.get('bot', 'questId')
  
def loadBattleType():
  return config.get('bot', 'typeId')

def loadBotSleepTime():
  return int(config.get('bot', 'apcost')) * 8

def generateTimestamp():
  return hex(int(time.time() * 1000)).lstrip('0x')

def generateBattleTime():
  return str(random.uniform(3,10))[0:4]

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
      queryString += '&' + key + '=' + in_queryString[key]
    
  response = None
  commandString = '%s "%s%s%s"' % (curlCommand, _server_host, path, queryString)
  response = json.loads(os.popen(commandString).read())
  if response['res'] != 0:
    print 'API error'
    print commandString
    print response
  return response

def getPlayerStatus():
  return apiRequest('/user/all_data')

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
  
def battleWin(questId):
  queryString = {}
  queryString.update({'qid' : questId})
  queryString.update({'res' : '1'})
  queryString.update({'time': generateBattleTime()})
  queryString.update({'d': '1'})
  queryString.update({'s': '1'})
  return apiRequest('/quest/result', queryString)
  
def battle(typeId, questId):
  response = battleInit(typeId, questId)
  if response['res'] == 0:
    print 'battle inital completed'
    time.sleep(60)
    response = battleWin(questId)
    if response['res'] == 0:
      print 'battle win - %s' % questId
      if response.has_key('earns'):
        print 'EXP: %s / GOLD: %s + %s' % (response['earns']['exp'], response['earns']['gold'], response['earns']['bonus_gold'])
      if response.has_key('quest_reward'):
        print 'QUEST REWARD!!!'
        print response['quest_reward']
      
def bot_mode():
  sleepTime = loadBotSleepTime()
  while True:
    currentSleepTime = 0
    typeId = loadBattleType()
    questId = loadBattleId()
    battle(typeId, questId)
    while currentSleepTime < sleepTime:
      playerStatus = getPlayerStatus()
      print 'exp: %s/%s' % (playerStatus['body'][4]['data']['disp_exp'], playerStatus['body'][4]['data']['next_exp'])
      print 'stamina: %s/%s' % (playerStatus['body'][4]['data']['staminaMax'] - (playerStatus['body'][4]['data']['stmRefillTime'] - int(time.time())) / 60 / 8, playerStatus['body'][4]['data']['staminaMax'])
      print 'sleep: %s/%s' % (currentSleepTime, sleepTime)
      time.sleep(60)
      currentSleepTime += 1
