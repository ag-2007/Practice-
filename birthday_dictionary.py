birthdays={"anika":"20/07/2007", "jake":"09/07/2008","jill":"03/03/2006"}
print("Welcome to the birthday dictionary! We know the birthdays of :")
for key in birthdays.keys():
    print(key.capitalize())
request=input("Whose birthday would you like to know : ").lower()
print(f"{request.capitalize()}'s birthday is on {birthdays[request]}")
