# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 14:13:28 2017
ASSIGNMENT 3

@author: JOHN MOHD BHAT
"""
import pandas as pd
import numpy as np
import matplotlib as plt
'''
1.Create two dataframe and Perform all join Operation,
 Concatenation and Append df1 to df4
'''
df1=pd.DataFrame({"A":["A0","A1","A2","A3"],"B":["B0","B1","B2","B3"],"C":["C0","C1","C2","C3"],"D":["D0","D1","D2","D3"]})

i=[0,1,2,3]
df1.index=(i)


df2=pd.DataFrame({"B":["B2","B3","B6","B7"],"D":["D2","D3","D6","D7"],"F":["F2","F3","F6","F7"]})

i=[2,3,6,7]
df2.index=(i)

'''
left join
'''
merged1=pd.merge(df1,df2,on="B",how="left")

'''
right join
'''
merged1=pd.merge(df1,df2,on="B",how="right")

'''
inner join
'''
merged1=pd.merge(df1,df2,on="B")

'''
full outer join
'''
merged1=pd.merge(df1,df2,how="outer")



'''
concatenation
'''
df3=pd.concat([df1,df2])
print df3

df4=df1.append([df2])
df4


'''
3.Write a function that returns the cumulative sum of numbers in a list. 
For example, if the function is given the list [1,2,3,4,5],
 it should return the list [ 1, 3, 6, 10, 15].
 '''
s=[]
f=0
def cum(x):
    global s,f
    g=0
    for i in range(0,len(x)):
        f=x[i]
        s.append(f+g)
        g=s[i]
    return s
cum([1,2,3,4,5])  


'''
4. Rewrite f = lambda x: x**2 as a regular function also called f using def.
'''

def sq(x):
    return(x**2)
sq(2)

'''
5. Find the second largest number in this
 list [ 9, 61, 2, 79, 58, 87, 68, 83, 61, 13]
 ''' 
x=[ 9, 61, 2, 79, 58, 87, 68, 83, 61, 13] 

sorted(x)[-2] 


    



'''
Q6
use arange with reshape method 
'''

a=np.arange(100)
a=a.reshape(10,10)+1

print(a)

'''
a)	Use the array object to get the number of elements, rows and columns
'''
a.shape

'''
b)	Get the mean of the rows and columns
'''

a.mean(axis=0) '''  mean of each row'''
a.mean(axis=1)  '''mean of each column'''


'''
c)	What do you get when you do this
'''
a[4,:]




'''
Read train.csv and explore Data, Fill missing values in the column age, embarked

column and drop column ‘name’,’sex’,’ticket’,’cabin’,’passengerID’ in train datasets

'''
#importing csv file
data=pd.read_csv('C:/Users/admin/Desktop/python/train_2.csv')

data.describe()

data.head
 '''  
 to get the missing values
 by default axis =0 i.e row operation'''
 
data.apply(lambda x:sum(x.isnull()),axis=0)

'''
replacing nans with median of age column
'''
data["Age"].fillna(data["Age"].median(),inplace=True)

'''
replacing nans with mode of Embarhed column
'''

data['Embarked'].value_counts()

data['Embarked'].fillna("S",inplace=True)



'''
dropping columns
'''
data_new=data.drop(["Name","Sex","Ticket","Cabin","PassengerId"],axis=1)

