import random

final_num = random.randint(1,10)
print("Hello let's play a game, I have chosen a number form 1 to 10 and you have to guess it")
trials = 0
guess = " "

while guess!=final_num:
    while True:
        try :
            guess = int(input("Guess a number between 1 and 9: "))
            if guess >= 1 and guess <= 9:
                break
            else:
                print("Your input must be a number between 1 and 9 inclusive")
        except ValueError:
            print("It must be a number")
    trials += 1
    if guess>final_num:
        print("Too high")
    elif guess<final_num:
        print("Too low")
    else:
        break

print(f"Congrats! You got it in {trials} tries")