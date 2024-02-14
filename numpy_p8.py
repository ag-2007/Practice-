import numpy as np 

s1='Anika is my name '
s2='I am an Indian'

print(np.char.add(s1,s2))
print(np.char.upper(s1))
print(np.char.lower(s1))


print(np.char.split(s1))
##splits whereever there is space

##splitlines is wherever there is a new character
s3 = "I live in \nCoimbatore"
print(np.char.splitlines(s3))

# It replaces the second parameter with the third
print(np.char.replace(s1,'name','surname'))

# If you need to print something like ****hi******
print(np.char.center('hi', 40, "*"))

