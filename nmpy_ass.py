# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 01:32:21 2017

@author: john
"""

#1.Create two dimensional array with 4 columns[1,2,3,4],[5,6,7,8]

import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])

''''
2. Display row sum and Column sum of above matrix.
'''
np.sum(a,axis=0) #column sum
np.sum(a,axis=1)#row sum


'''
Create 3*3 matrix using arange function.
'''

import numpy as np
x= np.arange(9).reshape(3,3)
print x



'''
4. a = [0,1,2,3,4,5,6,7,8,9] using Slicing Display even and odd no in a list
'''
a = [0,1,2,3,4,5,6,7,8,9] 
a[::2]
a[1::2]


'''
5. Create a matrix of order 3*3 find determinant, Eigen values, transpose the matrix.
'''
x= np.arange(9).reshape(3,3)
np.linalg.det(x)  #determinant of x
np.linalg.eigvals(x) #eigen values of x
x.T  #transpose of x



'''
6.Demonstatre all the statistical function take 20 uniform distribution values as a input.
'''

x=np.random.uniform(1,10,20)
np.mean(x)
np.median(x)
np.max(x)
np.min(x) 
np.std(x)
np.var(x)

