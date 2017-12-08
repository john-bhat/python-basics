# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:29:10 2017

@author: admin
"""

import pandas as pd

df2=pd.read_csv('C:/Users/admin/Desktop/python/input.csv')

df2
import html5lib
df=pd.read_html('https://www.safaribooksonline.com/library/view/python-fordata/9781449323592/ch04.html',header=0)

 df

 
 df=pd.read_html('https://www.latlong.net/category/cities-102-15.html',header=0)[0]

 df1=df.sort_values(["lat"])
 df2=df.sort_values(["long"],ascending=False)
 from pandas import ExcelWriter
 writer = ExcelWriter('C:/Users/admin/Desktop/python/demo.xlsx') 
 df.to_excel(writer,'Sheet1')
 df1.to_excel(writer,'Sheet2')
 df2.to_excel(writer,'Sheet3')
 writer.save()
 

