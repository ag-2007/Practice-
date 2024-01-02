birthdays={"Anika":"20/07/2007", "Jake":"09/07/2008","Jill":"03/03/2006"}
print("Welcome to the birthday dictionary! We know the birthdays of :")
for key in birthdays.keys():
    print(key)
request=input("Whose birthday would you like to know : ")
print(f"{request}'s birthday is on {birthdays[request]}")
