# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:35:44 2017

@author: admin
"""
import os
c=os.getcwd()
os.chdir("C:/Users/admin/Desktop/python")
'''
fibbonacci sum
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
fib(10)

'''
itterative method
'''
def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new
    
    
'''
adding memory to recursive functions to save intermidiate values to make it faster
than itterative methods
'''
memo = {0:0, 1:1}

def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]



