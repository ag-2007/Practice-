import random

words=[]
SOWPODS="D:\Anika Gupta\Others\IAMNEO\Coding\Practice python\Exercises\pick_a_word\SOWPODS.txt"
with open(SOWPODS, 'r') as f:
    line = f.readline().strip()
    while line:
      line = f.readline().strip()
      words.append(line)

random_index = random.randint(0, len(words)-1)
print("Random word: ", words[random_index])


