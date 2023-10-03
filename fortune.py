# Write your code here :-)
import random

def getAnswer(answerNumber):
    if answerNumber==1:
        return 'You will have a good life'
    elif answerNumber==2:
        return 'There is a high chance you will have a good life'
    elif answerNumber==3:
        return 'You might die earlier than others'
    elif answerNumber==4:
        return 'Your time is coming to an end'
    elif answerNumber==5:
        return 'You are going to die tomorrow'

print (getAnswer(random.randint(1,5)))
