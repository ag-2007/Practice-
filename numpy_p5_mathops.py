import numpy as np 

a=np.arange(0,18).reshape((6,3))
b=np.arange(20,38).reshape((6,3))
#print(a)
#print(b)

#print(a+b)
#print(np.add(a,b))

#print(a-b)
#print(np.subract(a,b))

#Multiplication.. not equal to matrix multiplication
#print(a*b)
#print(np.multiply(a,b))  

#Division
#print(a/b)
#print(np.divide(a,b))

#Matrix multiplication (@ symbol doesn't work... function also doesn't work)
#b.reshape((3,6))
#print(a.dot(b))

print(b.max())
print(b.min())
#argmax will return the index
print(b.argmax())

#here the axis means rows... axis =0 means columns
print(np.sum(b,axis=1))

#mean
print(np.mean())

#sqrt
print(np.sqrt())

#standard deviation
print(np.std(b))

#logarithm
print(np.lob(b))











