# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:45:00 2017

@author: admin
"""


import subprocess
def disk (partition="/"):
     info = subprocess.call(["df", partition]) 
     