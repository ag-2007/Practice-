import numpy as np

#empty array... contains two params, tupple and dtype... outputs with randomly generated numbers 
print(np.empty((3,3),int))

# getting an array with ones only - np.ones
print(np.ones(8))

#np.ones but also in the same format as the empty array
print(np.ones((2,2),int))

#np.zeros - array with only zeroes
print(np.zeros((2,3), int))


#data type can also be string/boolean but you may get empty strings and false values
