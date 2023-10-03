# Write your code here :-)
import random
secretNumber=random.randint(1,20)
print ('I am thinking of a number between 1 to 20')

for guessesTaken in range (1,7):
    print('Take a guess')
    guess=int(input())

    if guess>secretNumber:
        print('Nope too high')

    elif guess<secretNumber:
        print('Nope too low')
    else:
        break

if guess==secretNumber:
    print('Haha that is my number, you guessed it in '+str(guessesTaken)+' tries')
else:
    print('Too bad, it was'+ str(secretNumber))
