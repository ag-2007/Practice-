name=input("Hello, Please enter your name : ")
print("Wonderful, now enter your age and let me tell you the year you will turn a 100")
age= int(input())
year=2023+(100-age)
print("So "+ name + " ,you will turn 100 in the year " + str(year))
print ("Let's play another game")
repeat = int(input ("Enter a number here : "))

for i in range (0,repeat):
    print("Lets play another game" + "\n")
