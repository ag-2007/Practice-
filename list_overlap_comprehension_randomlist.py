import random
a=[random.randint(1,15 ) for _ in range(9)]
b=[random.randint(1,15 ) for _ in range(8)]
c=[num for num in a for numb in b if num==numb]
print (a)
print (b)
print(c)