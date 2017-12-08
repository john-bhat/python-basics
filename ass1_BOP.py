# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:07:02 2017

@author: admin
"""

#1. a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


#a)	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
k=[]
for i in a :
    if i<5:
        k.append(i)
print k        

#b)	Write this in one line of Python.
 k=[i for i in a if i<5]
print k
''' #c)	Ask the user for a number and return a list that contains only elements 
 from the original list a that are smaller than that number given by the user.
'''
x=int(input("enter the number  "))
k=[]
k=[i for i in a if i<x]
print k




#2. a = [5, 10, 15, 20, 25, 30, 35, 40]   Slice 20 and  25 using slicing.

a = [5, 10, 15, 20, 25, 30, 35, 40] 

a[3:5]

#3.Write a Program to display Fibonacci series <1000 and value separated by commas.

from __future__ import print_function

x=1000
a,b=0,1
sum=0
while sum<x:
        sum=a+b
        print(a,end=",")
        a=b
        b=sum
        
 '''       
 #4. Create a program that asks the user to enter their name and their age

 Print out a message addressed to them that tells them the year that they will turn 100 years old.       
   '''

import datetime
a =input("Enter your name ")  


diff=100-b
today = datetime.date.today()
fin=today.year + diff

print("you will turn 100 years old in year ",fin)


'''

5. Ask the user for a string and print out whether this string is a p
alindrome or not. (A palindrome is a string that reads the same forwards and backwards.)   
'''
a="boooob"
cnt=0
for i in range(len(a)/2):
    if a[i]==a[-i-1]:
        cnt+=1
if cnt==len(a)/2:
     print ("string is pallindrome")
else:
     print ("string is not pallindrome")
     
     
     
     
'''
6. Use for loop to calculate the sum of 1, 2, 3, …, 100 odd number.
'''     
sum=0     
for i in range(100):
    if i %2!= 0:
        sum+=i
print(sum)        


'''
7. Assign a string “GIS Programming” to a string variable. Print all the letters
 (in uppercase) line by line and calculate length and display in reverse order
'''
str1="GIS Programming"
str1=str1.upper()
len1=0
for i in str1:
    print i
    len1=len1+1
    
print "Lenght of String : ",len1
print "Reverse of String is ",str1[::-1]