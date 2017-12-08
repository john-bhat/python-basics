# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 07:47:41 2017

@author: admin
"""


'''
Quick Sort

'''

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(left ,middle ,right)
    return quicksort(left) + middle + quicksort(right)
    
print quicksort([3,4,8,7,6,1,2])



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return   quicksort(right)+ middle +quicksort(left)
    
print quicksort([3,6,8,1,2,3,7,8,12,22,10,1,2,1])
