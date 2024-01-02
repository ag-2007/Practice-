import random

words = []
SOWPODS = "D:\\Anika Gupta\\Others\\IAMNEO\\Coding\\Practice python\\Exercises\\guess_letters\\SOWPODS.txt"

with open(SOWPODS, 'r') as f:
    line = f.readline().strip()
    while line:
        line = f.readline().strip()
        words.append(line)

random_word = words[random.randint(0, len(words) - 1)]

print("Welcome to hangman")
hangman = ["_" for x in range(len(random_word))]
print(" ".join(hangman))

while "_" in hangman:
    usr_inp = input("Guess a letter or enter 'break' to quit: ")

    if usr_inp == "break":
        break

    correct_guess = False

    for i, letter in enumerate(random_word):
        if letter == usr_inp:
            hangman[i] = usr_inp
            correct_guess = True

    if correct_guess:
        print(" ".join(hangman))
    else:
        print("INCORRECT!")

print(f"The word was {random_word}")





   
   