import random

def game(a,b):
    cows=0
    bulls=0
    for x in range (0,4):
        if a[x] == b[x]:
            cows=cows+1
        elif a[x] in b:
            bulls=bulls+1
    return (str(cows)+ " Cows and " +str(bulls)+" Bulls")

if __name__=="__main__":
    print("Welcome to the cows and bulls game")
    usr_inp=" "
    guesses=0
    final=str(random.randint(1000,9999))
    while usr_inp!=final:  
        if usr_inp==final:
            break
        usr_inp=str(input("Enter your 4 digit guess : "))
        result=game(usr_inp,final)
        print (result)
        guesses=guesses+1
    print("Congrats you got it in "+str(guesses)+" tries!!")

    








