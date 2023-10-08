import random
People = ['Anu','Nads','Varsha','Jei','Dhruv','Rohit']
random.shuffle(People) #Not necessary but just trying the function out
print(People)
print ('I am going to guess your closest freind')
guess=random.choice(People)
print (guess + ' -This person is your closest friend right ?' )
response=input()

while response=="No" :
    guess=random.choice(People)
    print (guess + ' -This person is your closest friend right ?' )
    response=input()
    if response=='Yes':
        break

print ('Yay')






