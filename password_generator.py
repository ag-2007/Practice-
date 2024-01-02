import string
import random

def pwd_gen(size=8,char=string.ascii_letters+string.digits+string.punctuation):
    return "".join(random.choice(char) for _ in range (size))

print(pwd_gen(int(input("How many characters in your password ?"))))