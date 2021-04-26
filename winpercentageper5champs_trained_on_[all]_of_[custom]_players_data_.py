# -*- coding: utf-8 -*-
"""winpercentageper5champs_trained_on_[all]_of_[custom]_players_data_

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c8joDsO6B-DR-AfxbUpW_qMyC8WskgX2
"""

import numpy as np
import requests
import pandas as pd
import urllib.request, json 
import pandas as pd
import sys 
import time

with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json") as url:
    ChampList = json.loads(url.read().decode())

ChampDict = {}

for champ in ChampList['data']:
  # print(ChampList['data'][champ]['name'])
  # print(ChampList['data'][champ]['key'])
  ChampDict[champ] = ChampList['data'][champ]['key']

#print(ChampDict)

columns = ['C1', 'C2', 'C3', 'C4', 'C5', 'Result']
DF = pd.DataFrame(columns = columns)
MYAPIKEY = "RGAPI-33b13693-9d78-4e0a-85ff-a1a1070ebbfb"

SummonerNameArray = []
summonerName = input("Enter summoner name[s]")
SummonerNameArray.append(summonerName)
while True:
    if summonerName is "":
      break
    else: 
      summonerName = (str)(input('Summoner Name[s]'))
      if summonerName != '':
        SummonerNameArray.append(summonerName)

print(SummonerNameArray)

for summonerName in SummonerNameArray:
  time.sleep(2)
  url= "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + MYAPIKEY
  params={'APPID': MYAPIKEY}
  response=requests.get(url,params=params)
  values=response.json()
  print(values)
  time.sleep(2)
  #print(values['accountId'])
  accountId = values['accountId']
  #print(accountId)

  matchlistsurl = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + MYAPIKEY
  matches = requests.get(matchlistsurl, params)
  matchesdata = matches.json()
  #print(matchesdata)

  GamesArr = []
  ChampionArr = []


  # url = "http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json"
  # response = urllib.urlopen(url)
  # data = json.loads(response.read())
  # print(data) 

  matchlist = matchesdata['matches']
  for match in matchlist:
      #print(match)
      for x in match:
          if (x == 'gameId'):
              GamesArr.append(match[x])
          elif (x == 'champion'):
              ChampionArr.append(match[x])

  print(GamesArr)
  print(ChampionArr)

  AcceptedQueueTypes = [0, 420, 440, 700]
  for games in GamesArr:
      gameurl = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(games) + "?api_key=" + MYAPIKEY
      #print(gameurl)
      game = requests.get(gameurl, params)
      ParticipantsArr = []
      
      gamedata = game.json()
      #print(gamedata)
      isRanked = 0
      for x in gamedata:
        print(x)
        #print(x['queueId'])
        if (x == 'queueId'):
          if (gamedata[x] in AcceptedQueueTypes):
            isRanked = 1
        if (x == 'participants' and isRanked == 1):
          #print(gamedata[x])
          ParticipantsArr = gamedata[x]
      
      #print(ParticipantsArr)
      DefeatChamps = []
      VictoryChamps = []
      #temp = []
      for x in ParticipantsArr:
          #print(x)
          #print(x)        
          if ('participantId' in x):
            #print(x['participantId'])
            if (x['championId'] > 0):
              if (x['stats']['win'] == False):
                #print(x['championId'])
                for i, (key,value) in enumerate(ChampDict.items()):
                  if (str(x['championId']) == str(value)):
                    DefeatChamps.append(i)
                    #print(key)
                # if (x['championId'] in ChampDict.items()):
                #   DefeatChamps.append(ChampDict)   
              elif (x['stats']['win'] == True):
                #print(x['championId'])
                for i, (key,value) in enumerate(ChampDict.items()):
                  if (str(x['championId']) == str(value)):
                    VictoryChamps.append(i)
                  #  print(key)
                  #VictoryChamps.append(int(x['championId']))
      
      #print(DefeatChamps)
      #print(VictoryChamps)
      DefeatChamps = np.array_split(DefeatChamps,5)
      #if (len(str(int(DefeatChamps[0].astype(int)))) > 0):
      #  print(int(DefeatChamps[0].astype(int)))
      #print('---DEFEAT---')
    
      #DefeatChamps = str(DefeatChamps)
      # for x in DefeatChamps:
      #   if (len(DefeatChamps[0]) > 0):
      #     print(DefeatChamps[0][0])
      #     print(DefeatChamps[1])
      #     print(DefeatChamps[2])
      #     print(DefeatChamps[3])
      #     print(DefeatChamps[4])     

      #mylen = np.vectorize(len)
      #print(len((DefeatChamps))
      #if (mylen(str(DefeatChamps)) != '130'): 
      if (len(DefeatChamps[0]) > 0):
        new_row = {'C1':DefeatChamps[0][0], 'C2': DefeatChamps[1][0], 'C3': DefeatChamps[2][0], 'C4': DefeatChamps[3][0], 'C5':DefeatChamps[4][0], 'Result':0}
        DF = DF.append(new_row, ignore_index=True)   
      
      
      VictoryChamps = np.array_split(VictoryChamps,5)
      #print('--VICTORY--')
      #print(VictoryChamps[0])
      #print(VictoryChamps)
      if (len(VictoryChamps[0]) > 0):
        new_row = {'C1':VictoryChamps[0][0], 'C2':VictoryChamps[1][0], 'C3': VictoryChamps[2][0], 'C4': VictoryChamps[3][0], 'C5':VictoryChamps[4][0], 'Result':1}
        DF = DF.append(new_row, ignore_index=True)          

DF = pd.DataFrame(DF)
DF



X = DF.iloc[:, :5]
Y = DF['Result']

X

import numpy as np
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print(np.shape(X_train))
    print(np.shape(X_test))
    print(np.shape(y_train))
    print(np.shape(y_test))

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D, Dropout

print(len(ChampDict.keys()))

X_train = to_categorical(X_train, 155)
X_test = to_categorical(X_test, 155) 

#print(X_train)
print(np.shape(y_test))

y_test

#MLP model
import tensorflow.keras as TFKS

model = Sequential()

# Use your own hidden layer size
model.add(TFKS.Input(shape=(5,155)))
#model.add(Flatten())
model.add(Dense(16, activation='softmax'))
model.add(Dense(6, activation= 'softmax'))

model.add(Flatten())
model.add(Dense(1, activation = 'sigmoid'))


model.summary()

from tensorflow.keras.optimizers import Adam

opt = Adam(lr=0.001, decay=1e-7)

model.compile(loss='binary_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

import tensorflow as tf
X_train = np.asarray(X_train).astype('float32')
X_test = np.asarray(X_test).astype('float32')
y_train = np.asarray(y_train).astype('float32')
y_test = np.asarray(y_test).astype('float32')

Xtrain = tf.convert_to_tensor(X_train)
Xtest = tf.convert_to_tensor(X_test)
Ytrain = tf.convert_to_tensor(y_train)
Ytest = tf.convert_to_tensor(y_test)
print(np.shape(Xtrain))
print(np.shape(Xtest))

from tensorflow.keras.callbacks import EarlyStopping
es = EarlyStopping(monitor = 'val_accuracy',mode='max',patience=300,restore_best_weights=True,verbose=1)


Monitor = model.fit(Xtrain, y_train,
              batch_size= 10,
              epochs= 500,
              validation_data=(Xtest, y_test),
              callbacks = [es],
              shuffle = True)

print(model.predict(Xtest))
Predictions = np.round(model.predict(Xtest),0)

print(np.mean(model.predict(Xtest)))
print(Ytest)
#Ytest
#X= tf.convert_to_tensor(X)
#print(np.round(model.predict(Xtest)),2)
#arr = np.round((model.predict(Xtest)),0)
#print(arr)
#print(type(Ytest.numpy()))
#yarr = Ytest.numpy()
#np.round(model.predict(Xtest),0) - Ytest
#print(pd.DataFrame(abs(arr) - abs(yarr)))
#print(Predicted)
#print(Ytest)
Predictions = np.round(model.predict(Xtest), 0)
print(Predictions[0])
print(Ytest.numpy()[0])

print(type(Predictions))
print(type(Ytest.numpy()))
#model.evaluate(Xtest,Ytest)
from sklearn.metrics import confusion_matrix
confusion_matrix(Ytest, Predictions)

model.evaluate(Xtest,Ytest)

#convert Champion names to tensor
TeamComp = input("Enter 5 champions:")

TestChampArray = TeamComp.split()
NumericalChamps = []

for x in TestChampArray:
  if x in ChampDict.keys():
    #print(list(ChampDict.keys()).index(x))
    NumericalChamps.append(list(ChampDict.keys()).index(x))
    #print(ChampDict[x])
    #print("Hi")

NewDataFrame = pd.DataFrame(columns = ['C1', 'C2', 'C3', 'C4', 'C5'])
new_row =  {'C1': NumericalChamps[0], 'C2': NumericalChamps[1], 'C3': NumericalChamps[2], 'C4': NumericalChamps[3], 'C5': NumericalChamps[4]}
NewDataFrame = NewDataFrame.append(new_row, ignore_index=True)   

NewDataFrame
#Convert to categorical


NewDataFrame = to_categorical(NewDataFrame, 155)

NewDataFrame = np.asarray(NewDataFrame).astype('float32')
NewDataFrame = tf.convert_to_tensor(NewDataFrame)
#for i, (key,value) in enumerate(ChampDict.items()):
  
print(model.predict(NewDataFrame))



#print(ChampDict)