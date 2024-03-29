import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips=[]
    outcomes=['heads','tails']
    for i in range(100):
        result=random.choice(outcomes)
        coin_flips.append(result)


    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak_count = 0
    for i in range(len(coin_flips) - 5):
        if all(coin_flips[i + j] == coin_flips[i] for j in range(6)):
            streak_count += 1

    if streak_count > 0:
        numberOfStreaks += 1
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
