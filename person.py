# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:27:16 2017

@author: admin
"""

class Person(object):
    def __init__(self, name, age):
          self.name = name
          self.age  = age
   
    def __repr__(self): 
        return "Name: %s , Age: %d \n"  % (self.name, self.age) 

class City(object):
    def __init__(self,population,country):
        self.population=population
        self.country=country
    def __repr__(self):
        return ("Population: %d,  country: %s \n" %(self.population,self.country))