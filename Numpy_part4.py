import numpy as np 

a=np.arange(1,51)
a=a.reshape((10,5))
#print(a)

#[rows, column} format
print(a[0])
print(a[2])
print(a[0,0])
print(a[3,4])

# Colon from where to where... only colon means all the rows
print(a[2:5])
print(a[0:10])

#colon with a third parameter represents column
print(a[:, 2])
print(a[2:5, 2])

#All rows certain columns
print(a[:, 2:5])




