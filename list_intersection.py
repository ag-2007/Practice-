import random

a = [random.randint(1, 20) for _ in range(random.randint(5, 10))]
b = [random.randint(1, 20) for _ in range(random.randint(5, 10))]
print(a, b)

c=set(a).intersection(set(b))
print(list(c))