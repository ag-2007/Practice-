import random

final_num = random.randint(1,10)
print("Hello let's play a game, I have chosen a number form 1 to 10 and you have to guess it")
trials = 0
guess = " "

while guess!=final_num:
    guess=int(input("Enter your guess: "))
    trials = trials+1
    if guess>final_num:
        print("Too high")
    elif guess<final_num:
        print("Too low")
    else:
        break

print("Congrats! You got it in " + str(trials) + " tries")




