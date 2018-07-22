# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 22:50:26 2018

@author: Logan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('LabelledDataset.csv')
dataset.head()
#theano+tensorflow=keras

x= dataset.iloc[:,0:46].values
y= dataset.iloc[:,217].values
m=[]
n=[]              
a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]              
e=input('Enter the contienent hosting the worldcup \n')

f=input('enter 1 if the worldcup is of the form group a and group b,0 if the worldcup happens as a single group \n')
f=int(f)
if f==1:
   z=input('enter the no of teams in group a \n')
   z=int(z)
   w=input('enter the no of teams in group b \n')
   w=int(w)
   print('enter 1 for afgh \n')
   print('enter 2 for aus \n') 
   print('enter 3 for bangladesh \n')
   print('enter 4 for bermuda \n')
   print('enter 5 for can \n')
   print('enter 6 for east africa \n')
   print('enter 7 for england \n')
   print('enter 8 for hongkong \n')
   print('enter 9 for india \n')
   print('enter 10 for ireland \n')
   print('enter 11 for kenya \n')
   print('enter 12 for Namibia \n')
   print('enter 13 for Netherlands \n')
   print('enter 14 for New zeland \n')
   print('enter 15 for P.N.G \n')
   print('enter 16 for Pakistan \n')
   print('enter 17 for scotland \n')
   print('enter 18 for South africa \n')
   print('enter 19 for srilanka \n')
   print('enter 20 for UAE \n')
   print('enter 21 for USA \n')
   print('enter 22 for WEST INDIES \n')
   print('enter 23 for Zimbabwe \n')
   print('enter the teams in group a')
   for k in range(0,z):
      d=input('enter the country')
      m.append(d)
   for k in range(0,z):
        if m[k]=='1':
            a[0]=1
        elif m[k]=='2':
            a[1]=1
        elif m[k]=='3':
            a[2]=1
        elif m[k]=='4':
            a[3]=1
        elif m[k]=='5':
            a[4]=1
        elif m[k]=='6':
            a[5]=1
        elif m[k]=='7':
            a[6]=1
        elif m[k]=='8':
            a[7]=1
        elif m[k]=='9':
            a[8]=1
        elif m[k]=='10':
            a[9]=1
        elif m[k]=='11':
            a[10]=1
        elif m[k]=='12':
            a[11]=1
        elif m[k]=='13':
            a[12]=1
        elif m[k]=='14':
            a[13]=1
        elif m[k]=='15':
            a[14]=1
        elif m[k]=='16':
            a[15]=1
        elif m[k]=='17':
            a[16]=1
        elif m[k]=='18':
            a[17]=1
        elif m[k]=='19':
            a[18]=1
        elif m[k]=='20':
            a[19]=1
        elif m[k]=='21':
            a[20]=1
        elif m[k]=='22':
            a[21]=1
        elif m[k]=='23':
            a[21]=1
   print('enter the teams in group b')
   for k in range(0,z):
       u=input('enter the country')
       n.append(u)
   for k in range(0,w):
         if n[k]=='1':
            a[24]=1
         elif n[k]=='2':
            a[25]=1
         elif n[k]=='3':
            a[26]=1
         elif n[k]=='4':
            a[27]=1
         elif n[k]=='5':
            a[28]=1
         elif n[k]=='6':
            a[29]=1
         elif n[k]=='7':
            a[30]=1
         elif n[k]=='8':
            a[31]=1
         elif n[k]=='9':
            a[32]=1
         elif n[k]=='10':
            a[33]=1
         elif n[k]=='11':
            a[34]=1
         elif n[k]=='12':
            a[35]=1
         elif n[k]=='13':
            a[36]=1
         elif n[k]=='14':
            a[37]=1
         elif n[k]=='15':
            a[38]=1
         elif n[k]=='16':
            a[39]=1
         elif n[k]=='17':
            a[40]=1
         elif n[k]=='18':
            a[41]=1
         elif n[k]=='19':
            a[42]=1
         elif n[k]=='20':
            a[43]=1
         elif n[k]=='21':
            a[44]=1
         elif n[k]=='22':
            a[45]=1    
    
elif f==0:
   z=input('enter the no of teams participating \n')
   z=int(z)
   w=z/2
   w=int(w)
   print('enter 1 for afgh \n')
   print('enter 2 for aus \n') 
   print('enter 3 for bangladesh \n')
   print('enter 4 for bermuda \n')
   print('enter 5 for can \n')
   print('enter 6 for east africa \n')
   print('enter 7 for england \n')
   print('enter 8 for hongkong \n')
   print('enter 9 for india \n')
   print('enter 10 for ireland \n')
   print('enter 11 for kenya \n')
   print('enter 12 for Namibia \n')
   print('enter 13 for Netherlands \n')
   print('enter 14 for New zeland \n')
   print('enter 15 for P.N.G \n')
   print('enter 16 for Pakistan \n')
   print('enter 17 for scotland \n')
   print('enter 18 for South africa \n')
   print('enter 19 for srilanka \n')
   print('enter 20 for UAE \n')
   print('enter 21 for USA \n')
   print('enter 22 for WEST INDIES \n')
   print('enter 23 for Zimbabwe \n')
   print('enter the teams in group a')
   for k in range(0,w):
      d=input('enter the country')
      m.append(d)
   for k in range(0,w):
        if m[k]=='1':
            a[0]=1
        elif m[k]=='2':
            a[1]=1
        elif m[k]=='3':
            a[2]=1
        elif m[k]=='4':
            a[3]=1
        elif m[k]=='5':
            a[4]=1
        elif m[k]=='6':
            a[5]=1
        elif m[k]=='7':
            a[6]=1
        elif m[k]=='8':
            a[7]=1
        elif m[k]=='9':
            a[8]=1
        elif m[k]=='10':
            a[9]=1
        elif m[k]=='11':
            a[10]=1
        elif m[k]=='12':
            a[11]=1
        elif m[k]=='13':
            a[12]=1
        elif m[k]=='14':
            a[13]=1
        elif m[k]=='15':
            a[14]=1
        elif m[k]=='16':
            a[15]=1
        elif m[k]=='17':
            a[16]=1
        elif m[k]=='18':
            a[17]=1
        elif m[k]=='19':
            a[18]=1
        elif m[k]=='20':
            a[19]=1
        elif m[k]=='21':
            a[20]=1
        elif m[k]=='22':
            a[21]=1
        elif m[k]=='23':
            a[21]=1
   for k in range(0,w):
       u=input('enter the country')
       n.append(u)
   for k in range(0,w):
        if n[k]=='1':
            a[24]=1
        elif n[k]=='2':
            a[25]=1
        elif n[k]=='3':
            a[26]=1
        elif n[k]=='4':
            a[27]=1
        elif n[k]=='5':
            a[28]=1
        elif n[k]=='6':
            a[29]=1
        elif n[k]=='7':
            a[30]=1
        elif n[k]=='8':
            a[31]=1
        elif n[k]=='9':
            a[32]=1
        elif n[k]=='10':
            a[33]=1
        elif n[k]=='11':
            a[34]=1
        elif n[k]=='12':
            a[35]=1
        elif n[k]=='13':
            a[36]=1
        elif n[k]=='14':
            a[37]=1
        elif n[k]=='15':
            a[38]=1
        elif n[k]=='16':
            a[39]=1
        elif n[k]=='17':
            a[40]=1
        elif n[k]=='18':
            a[41]=1
        elif n[k]=='19':
            a[42]=1
        elif n[k]=='20':
            a[43]=1
        elif n[k]=='21':
            a[44]=1
        elif n[k]=='22':
            a[45]=1    
    
    
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/4,random_state=0)
 #fitting simple linear regression to the training set
 #feature scalling
from sklearn.preprocessing import StandardScaler
 
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(a)
print('the predicted country to win the 2019 worldcup is: ')
print(y_pred)