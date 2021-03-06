# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:15:59 2017

@author: admin
"""

import numpy as np

# height in inches, weight in pounds  
height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]

np_height = np.array(height)
np_weight = np.array(weight)


np_height_meters  = np_height  * 0.0254
np_weight_kgs = np_weight *  0.453592 

#print (m_height)
#print (k_weight)

# kg/m^2
 
np_height_meters_sqr  = np_height_meters ** 2
#print (msqr_height)

bmi = np_weight_kgs / np_height_meters_sqr 

print (bmi)

#######################################
# height in inches, weight in pounds  
height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]

m_height = [x * 0.0254 for x in height]
k_weight = [x * 0.453592 for x in weight]

#print (m_height)
#print (k_weight)

# kg/m^2
 
msqr_height = [x * x for x in m_height]
#print (msqr_height)

bmi  = [k_weight[i]/msqr_height[i] for i in range(len(msqr_height))]
print (bmi)








