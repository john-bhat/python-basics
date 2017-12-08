# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:25:55 2017

@author: admin
"""

import re
result=re.match(r'AS','AS analysts school AS')
print( result)
print (result.end())
print (result.group(0))


result=re.match(r'Analytics','AS Analysts school AS')
result

str="       this is the string  example.....wow!!!   "
print (str.rstrip())   #remove spaces from right



#if in the document has ist word Pyhton then onlyit will show the whole document

hand =open('C:/Users/admin/Desktop/python/t1.txt')
for line in hand:
    line=line.rstrip()
    if re.match("Python",line):
        print(line)
        
#search the entire document for given word if present then print whole document        
hand =open('C:/Users/admin/Desktop/python/t1.txt')
for line in hand:
    line=line.rstrip()
    if re.search("transparent",line):
        print(line)        
        
 
hand =open('C:/Users/admin/Desktop/python/t.txt')
for line in hand:
    line=line.rstrip()
    if re.search("hobby",line):
        print(line)        
        
        
        

import re

var="I work at Aegis, and harry@aegis.com is my email id Sachin.r.t.73@yahoo.com"

r=re.findall(r"\s[^.][A-Za-z0-9._%]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}",var)
print(r)
r1=re.search(r"[\w.]+@[\w.]+",var)      

print(r1.start())  #start of match
print(r1.end())    #end of match
print(r1.group())
   # matched string
print(r1.span())    # renge of indexes from start to end of matched string




#findall
hand =open('C:/Users/admin/Desktop/python/t1.txt')
line_all=""
for line in hand:
    line_all= line_all+ line.rstrip()
print (re.findall('Python',line_all))      


result=re.findall(r'AS','AS Analytics school AS')  

print(result)


print(re.findall(r'\d','here are 212 words'))
print(re.findall(r'\d+','here are 212 words'))
print(re.findall(r'\d{1,5}','here are 212 words'))

print(re.findall(r'\d{1,5}\s\w+','here are 212 words'))



import re
text='abbaabbbbaaaaa'
pattern="ab"

for match  in re.findall(pattern,text):
    print( 'found "%s"' %match)
    
    

exp='''Amit is 20 years old and Bhairav is 45 years old and his father, Dsarshan is 105
'''

ages=re.findall(r'\d{1,3}',exp)
names=re.findall(r'[A-Z][a-z]*',exp)
print ( ages)
print( names)  



a='Hello from csev@cjxj.com to hgc@ghv.fx about the meeting @2PM'
lst=re.findall("\S+@\S+",a)
print(lst)

lst=re.findall(r"(..)","aegis")  #..is for grouping


result=re.split(r'\s','here are some words') #splitting based on space
result=re.split(r'(\s*)','here are some words')  #splitting with spaces aklso
result=re.split(r'\s*','here are some words')


import yahoo_finance

from yahoo_finance import Share
yahoo=Share('aapl')   #goog nflx 
print (yahoo.get_open())
print (yahoo.get_price())
print (yahoo.get_trade_datetime())











        
        
  