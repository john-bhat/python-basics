# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:07:42 2017

@author: admin
"""

import pandas as pd

#creating series
s=[1,2,3,4]

n1=pd.Series([2,3,4,5,6,7])
print(n1)
i=["m","h","k","g"]

c=pd.Series(s,index=i)

c

#creating dictionary 
s2={"A":112,"B":23,"C":34}
ds=pd.Series(s2)
ds
type(ds)

#crwating dataframe
i=["m","h","k","g"]
n2=pd.DataFrame(s,index=i)
n2.columns=["col1"]
n2["marks"]=[58,23,4,5]
n2["marks"]=n2["marks"]+4
n2



df=pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]})
df



#to get 1 to 30 days of a month
dates=pd.date_range('20100101',periods=30,freq='D')
dates

#to get years
dates=pd.date_range('20100101',periods=12,freq='12m')
dates

#to get all months in a  year
dates=pd.date_range('20100101',periods=10,freq='M')
dates


import numpy as np

df=pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))
df

df.head
df.tail

# summary  of numerical of columns

df.describe()


#transpose
df.T

#sort by coulumn by default it is ascending order
df.sort_values(by="B")

#Descending Order
df.sort_values(by="B",ascending=False)

#multiple columns
df.sort_values(["B","C"],ascending=False)

#sort by 1 column
df["A"]


#slicing

df=pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]})
df

df.loc[0:2]
df.iloc[0:2]
df.ix[0:2,0:2] 
df.ix[1:2,['BBB','CCC']] #intersect
#C 1,2
df.iloc[:,[1,2]]

import numpy as np
df=pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
                 'B':['one','one','two','three','two','two','one','three'],
     'C': np.random.randn(8),
      'D':np.random.randn(8)})

print df.groupby('A').sum()

print df.groupby(['A','B']).sum()



#merge
df1=pd.DataFrame({'year':[2001,2002,2003,2004],'int_rate':[2,3,2,2],'us_gdp':[50,55,65,55]})

df2=pd.DataFrame({'year':[2001,2003,2004,2005],'int_rate':[7,6,5,4],'us_gdp':[50,52,60,53]})


merged=pd.merge(df1,df2,on='year')
merged.set_index('year',inplace=True)

merged

merged=pd.merge(df1,df2,on='year',how='left')
merged.set_index('year',inplace=True)
merged

'''
Create DataFrame and index it
'''
import pandas as pd
s={"paris":[0,3,6],"berlin":[1,7,4],"madrid":[2,5,8]}
i=["b","a","c"]
df=pd.DataFrame(s,index=i)
df
'''
OR
'''
df=pd.DataFrame({"paris":[0,3,6],"berlin":[1,7,4],"madrid":[2,5,8]})
df.index=i


'''sorting and ordering index level not values'''

df.sort_index([ascending=True]) 

df.sort_index(by="berlin")

df.sort_index(axis=0)   '''sort row wise index level'''
df.sort_index(axis=1)'''sort by column headers'''

df.drop("berlin",axis=1) '''always use axis =1 to drop any column'''
df.drop("berlin")  '''wrong command'''


'''statistical computation using panda also we can do by numpy'''
df.describe() '''summary of dataframe'''

df.sum(axis=1)   '''sum of all column values'''

df.cov()      '''covariance between columns'''

df.corr()    '''coreelation between columns'''


'''
applying function on entire dataframe by using applymap function and lambda 
''''

import numpy as np
import math
f=lambda x:sqrt(x)
df.applymap(f)

'''apply function on perticular column using lambda function'''
 
df.berlin=df["berlin"].map(f)

''' concatenation in pandas is the process either adding rows to the end of an 
existing series or dataframe or adding additional column to dataframe'''
import pandas as pd
s1=pd.Series(np.arange(0,3))
s2=pd.Series(np.arange(5,8))
pd.concat([s1,s2])




