# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:42:58 2017

@author: admin
"""
"""
1.	Create a dictionary that contain ten student name and mark of 5 
Subjects, display marks >50 students.
"""

import pandas as pd

dic={"name":["a","b","c","d","e","f","g","h","i","j"],"math":[20,45,66,78,87,54,90,53,34,73]
    ,"science":[87,54,90,53,34,73,40,45,66,78],"english":[53,34,73,40,45,87,54,90,66,78],"history":[45,87,54,90,66,53,34,73,40,78],"art":[53,34,73,40,45,87,54,90,66,78]}

dat=pd.DataFrame(dic)
dat["english">50]

dat.loc[dat["science"]>50]

 

"""
2.	Create Dataframe perform groupby operation animal and only display group of cat .
"""
dic={"adult":[False,False,False,False,False,True,True],"animal":["cat","dog","cat","fish","dog","cat","cat"],
     "size":["S","S","M","M","M","L","L"],"weight":[8,10,11,1,20,12,12]}

dat=pd.DataFrame(dic)

for name,group in dat.groupby("animal"):
   print( group[group.animal=="cat"])


'''
3.	Demonstrate the .loc[],.iloc[],.ix[] take above dataframe as a input.
'''   

dat.loc[0:2]
dat.iloc[0:2]
dat.ix[0:2,0:3] 
dat.ix[0:2,['animal','size']] #intersect
dat.iloc[:,[1,2]]


"""
4.	Demonstrate join, merge and append,concat operation. 
"""

d1=pd.DataFrame({"Eid":[1,2,3],"Ename":["Brijesh","pratik","Rafiur"],"Did":[10,30,50]},index=[0, 1, 2])
d2=pd.DataFrame({"Did":[10,30,40],"Dname":["IPF","HR","TIS"]},index=[3,4,5])

mr=pd.merge(d1,d2,on="Did")
mr=pd.merge(d1,d2,on="Did",how="left")
mr=pd.merge(d1,d2,on="Did",how="right")
#append
d2.append(d1)

#concat
f=[d1,d2]
pd.concat(f)

"""
5.	Take snsdata.csv file as input perform Data Exploration ,
 Data cleaning task,sort values of age column.
"""

sns=pd.read_csv('D:\PGP BA BD DS\BA BD & DS Material\R Language\Program\Assignment\SNS\snsdata.csv')
sns
print "Displaying Summary of SNS",sns.describe()
print sns.isnull()
print sns.isnull().values.any()
print sns.isnull().sum()
print sns.isnull().sum().sum()

yr26=sns.loc[sns['gradyear'].values==2006,]
yr27=sns.loc[sns['gradyear'].values==2007,]
yr28=sns.loc[sns['gradyear'].values==2008,]
yr29=sns.loc[sns['gradyear'].values==2009,]
yr26['gender']=yr26['gender'].fillna('F')
yr27['gender']=yr27['gender'].fillna('F')
yr28['gender']=yr28['gender'].fillna('F')
yr29['gender']=yr29['gender'].fillna('F')
yr26['age']=yr26['age'].fillna(19)
yr27['age']=yr27['age'].fillna(18)
yr28['age']=yr28['age'].fillna(17)
yr29['age']=yr29['age'].fillna(16)

sns=yr26.append([yr27,yr28,yr29])