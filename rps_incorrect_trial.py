import random
opposition = ""

def comp_choice(n):
    random.randint(1,3)
    if n==1:
        return ("Rock")
    elif n==2:
        return ("Paper")
    elif n==3:
        return ("Scissors")
    
def game(a,b):
    if a==b:
        print("It's a draw")
    elif a=="Rock" and b=="Scissors":
        print("You Win!")
    elif a=="Scissors" and b=="Rock":
        print("I Win!")
    elif a=="Paper" and b=="Rock":
        print("You Win!")
    elif a=="Rock" and b=="Paper":
        print("I Win!")
    elif a=="Scissors" and b=="Paper":
        print ("You Win!")
    elif a=="Paper" and b=="Scissors":
        print("I Win!")
    
while True:
    usr_inp = input ("Enter Rock, Paper or Scissors (or enter stop to quit) : ")
    if usr_inp =="stop":
        break
    opposition = comp_choice()
    print("Computer's choice:", opposition)
    game(usr_inp, opposition)
    


