import numpy as np 

#np.arange, very common, like for loop... np. arange(start, end, step(optional))
a = np.arange(2,20,4)
#print(a) commented out

#arr.reshape ((rows,column))
a=a.reshape((5,1))
#print(a) commented out

b=np.arange(1,100,2)
print(b)
b=b.reshape((10,5))
print(b)

#np.flatten() reverse of reshape... gives one row and multiple coloumns
print(b.flatten())

#ravel()  is similar but modifies original value while flatten does with a copy of original and is faster
print(b.ravel())