# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:59:42 2017

@author: John Bhat
"""
from nltk.tokenize import RegexpTokenizer

tokenizer=RegexpTokenizer('((\d{1,4}|\d{1,4}th)[^A-Z0-9](\d{1,2}|\w{1,10})[^A-Z0-9]\d{1,4})|(^([^.][A-Za-z0-9._%]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}))|(([A-Z][a-z]{6})[^a-zA-Z0-9]\d{4})')
hand =open('C:/Users/admin/Desktop/python/test-file.txt')
for line in hand:
    if tokenizer.tokenize(line)!=[]:
         l=tokenizer.tokenize(line)  #return list of tuple 
       #  print(l)
         for k in range(0,len(l)):      #get the matched string with max length 
            a=[]
            for i in l[k]:
               if len(a)<len(i):
                  a=i
            print (a)  

            