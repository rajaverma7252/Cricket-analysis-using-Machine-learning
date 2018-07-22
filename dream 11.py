# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:28:48 2018

@author: Logan"""

import sys 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_excel('batsmen.xlsx')
a=input("Enter the no of batsmen you want in indian team (between 5 to 7)\n")
a=int(a)
c=input("Enter the no of bowlers you want in indian team (not more than 6)\n")
c=int(c)

if a+c!=11:
    print("We need exactly 11 players to predict the best 11 players")
    sys.exit()
    
x= dataset.iloc[20:29,[1,4,6,8]].values
y= dataset.iloc[20:29,0].values
               
#fitting simple linear regression to the training set
#feature scalling
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
x=sc.fit_transform(x)

#predicting the test set resuts
#y_pred=classfier.predic

from sklearn.svm import SVC
df=SVC(kernel='rbf',random_state=0)
df.fit(x,y)
y_pred=df.predict(x)

s= []
for i in y_pred:
    if i not in s:
        s.append(i)
batsman=[]

for i in range(0,a):
    batsman.append(s[i])
    
#for bowlers
datas=pd.read_excel('bowler.xlsx')

d= datas.iloc[[20,21,22,23,24,25,26],[2,3,5,8]].values
e= datas.iloc[[20,21,22,23,24,25,26],0].values
                 
#c=input("enter the no of bowlers you want in indian team (not more than 6)\n")
#c=int(c)
             
#fitting simple linear regression to the training set
#feature scalling
from sklearn.preprocessing import StandardScaler
 
sc=StandardScaler()
d=sc.fit_transform(d)
 
#predicting the test set resuts
#y_pred=classfier.predic

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(d,e)
e_pred=classifier.predict(d)                        
                         
f = []
for i in e_pred:
    if i not in f:
        f.append(i)
bowler=[]
for i in range(0,c): 
    bowler.append(f[i])
                             
best=[]
for i in range(0,a):
    best.append(batsman[i])
    
for i in range(0,c):
    best.append(bowler[i])
    
print('The final list of best 11 players of the Indian cricket team is as follows \n' )
for i in range(0,11):
    print(best[i])  #to print the total no of players