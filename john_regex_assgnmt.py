# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:34:28 2017

@author: admin
"""

'''
1.	Employee number: 8888000012,Date: February 20, 2017
 Extract the Employee number and Date Using Regular Expression.
'''
y="Employee number: 8888000012,Date: February 20, 2017"

import re

r=re.findall(r'\d{10}',y)
print(r)

r1=re.findall(r'\w*\s\d{1,2},\s\d{4}',y)
print(r1)



'''
2.	data =["surname: Ambani, prename: Anil, profession: Businessman",
 "surname: Pandey, prename: Rahul, profession: Student"]Extract 
 surname ,prename ,profession in the list using re.
 '''
 
 
data =["surname: Ambani, prename: Anil, profession: Businessman",
 "surname: Pandey, prename: Rahul, profession: Student"]
 
for i in range(len(data)):
    rer=re.findall(r'[A-Z][a-z]*',data[i]) 
    print(rer)
    

'''
   3.	str=’’’Anand is Software Developer,his Salary:25000 and 
   email:a@gmail.com;Suraj is Data Scientist his Salary:50000 and
   email:s@gmail.com Extract Name,Salary and email using re 
   
 '''

str='''Anand is software developer,his salary:25000 and  email:a@gmail.com;Suraj is data scientist his salary:50000 and  email:s@gmail.com '''
rer=[]
new=re.split(';',str)
for i in range(len(new)):
   rer=[]
   rer.append(re.findall(r'[A-Z][a-z]*',new[i]) ) 
   rer.append(re.findall(r'\d{5}',new[i]) ) 
   re1=re.search(r"[\w.]+@[\w.]+",new[i])   

   rer.append(re1.group()) 
   print(rer)

   
   
'''

4.	Demonstrate all re Functions.
'''

#Reg
#Split the string and return  a splitted array.
#1
import re
result=re.split(r'y','Analytics')#y like separator
print result
#2
print re.split(r'\s','here are some words')
print re.split(r'(\s*)','here are some words')
print re.split(r'\s*','here are some words')

#Findall() Find all the occurancence(>1) of the pattern in the string
#1
result=re.findall(r'AS','AS Analytics School AS')
print result

#2
print re.findall(r'\d','here are 212 words')
print re.findall(r'\d+','here are 212 words')
print re.findall(r'\d{1,5}','here are 212 words')
print re.findall(r'\d{1,5}\s\w+','here are212 words')

#3
import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.findall(pattern, text):
    print 'Found "%s"' % match
    
#4
import re 
hand = open('t1.txt')
line_all = ""
for line in hand:
    line_all = line_all + line.rstrip()

print re.findall('Python',line_all)

#5
import re
exp='''Amit is 20 years old and  Bhairav is 45 years old
and his father,Dharshan is 105
'''
ages=re.findall(r'\d{1,3}',exp)
names=re.findall(r'[A-Z][a-z]*',exp)
print ages
print names

#6
import re
s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
lst = re.findall('\S+@\S+', s)
print lst

#7
m=re.findall(r"(..)","aegis")
m



#match() find match at start of the string
#1
result=re.match(r'AS','AS Analytics School AS')
print result.start()
print result.end()
print result.group(0)
#2
result=re.match(r'Analytics','AS Analytics School AS')
print result

#3
import re 
hand = open('t1.txt') 
for line in hand:
    line = line.rstrip()
    if re.match('Python',line):
        print line 



#Sub() replace the patter with the given replacement string
#1
result=re.sub(r'India','the world','AS Analytics India School AS')
print result

#2
import re 
hand = open('t1.txt')
line_all = ""
for line in hand:
    line_all = line_all + line.rstrip()

print re.sub('Python', 'C', line_all)


#Search Method
# search() Find match anywhere in the string
result=re.search(r'Analytics','AS Analytics School AS')
print result.group(0)
#1
import re 
hand = open('t.txt') 
for line in hand:
    line = line.rstrip()
    if re.search('hobby ',line):
        print line 

#2
import re 
var="I work at Aegis, and harry@aegis.com is my email id."
r1 = re.search(r"[\w.]+@[\w.]+",var)
print r1.group()
print r1.start()
print r1.end()
print r1.span()

#1
s="nicely lying,fly,jointly"
for m in re.finditer(r"ly\w+", s):
    print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))
    
#2    
import re
hand = open('t.txt')
line_all = ""
for line in hand:
    line_all = line_all + line.rstrip()
for m in re.finditer(r"\w+ly", line_all):
    print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))


   
import re
s="hello how are you 123 @ gmail .com "
s.rstrip()






'''
5.	Extract minimum five prices of stock market “goog aapl fb nflx tsla” from url http://finance.yahoo.com/

'''


import yahoo_finance

stock=["goog", "aapl", "fb","nflx", "tsla"]
from yahoo_finance import Share
open1=[]
price=[]

for lis in stock:
    
     yahoo=Share(lis)   #goog nflx 
     open1.append(yahoo.get_open())
     price.append(yahoo.get_price())  
     
combi=pd.DataFrame({"name":stock,"open":open1,"price":price})   

print(combi)
    


'''
Q6
•	Extract all the text from the file and print it
'''

data=open('C:/Users/admin/Desktop/python/babynames.txt')   
for line in data:
    print(line)
    
'''
•	Find and extract the year and print it
'''
data=open('C:/Users/admin/Desktop/python/babynames.txt')   
for line in data:
    p=re.findall(r'\d{4}',line)
    if p!=[]:
       print(p)
       
'''
'•	Extract the names and rank numbers and print them''. 
'''       
ra=""
data=open('C:/Users/admin/Desktop/python/babynames.txt')   
for line in data:
    ra=re.findall(r'[A-Z][a-z]*\s?\d{2,3}',line)
    if ra!=[]:
       print(ra)

'''
•	Extract Palindrome string and print them
'''

ra=""
data=open('C:/Users/admin/Desktop/python/babynames.txt')   
for line in data:
    ra=re.split(" ",line) 
    for i in ra:
        if len(i)!=1 :          
            a=len(i)/2
            w=i[0:a]
            y=i[a:len(i)]
            count=0    
            for j in range(a):
                if w[j]==y[-j-1]:
                    count +=1
            if count==a:
                print(i)
                
                
'''
•	Extract four character word and print it

'''
ra=""
data=open('C:/Users/admin/Desktop/python/babynames.txt')
for line in data:
    ra=re.findall(r'\s\w{4}\s',line)             
    print(ra)        
    
    
 
 data=open('C:/Users/admin/Downloads/Analytics Assignment/Events_Data.txt')   
import re
ra=[]
for line in data:
     if re.findall(r'"OfferID":"\d{5}"|"CustomerID":"\d{3}"',line) !=[]:
          re.subn('"',line,'')
          ra.append(re.findall(r'"OfferID":"\d{5}"|"CustomerID":"\d{3}"',line))
        #  ra.append(re.findall(r'"OfferID":"\d{5},"Category":"\d{5}","CustomerID":"\d{3}"',line)) 
        
     
print(ra)
       
x=re.split(r',',str(p))
(re.findall(r'\d{3}',x[2]))

s='jkvlhc mnlL ,jklb "OfferID":"21624","Category":"90000","CustomerID":"294"ncgky ,jhhclytd'


p=re.findall(r'"OfferID":"\d{5}"|"CustomerID":"\d{3}"',s)
