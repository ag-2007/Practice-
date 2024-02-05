import numpy as np 

#list is only 1D, np arrays can be multidimensional

print('1D array')
q = np.array([1,2,3,4,5])
print(q)

print('2D array')
d = np.array([[2,4,6,8],[1,3,5,7]])
print(d)

#type function
print(type(d))

#size 
print(q.size)

#shape
print(q.shape)

#datatype
print(q.dtype)

#transpose function switches rows with column and column with rows
print(d)
print(d.transpose())