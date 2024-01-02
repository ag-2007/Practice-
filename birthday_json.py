import json

birthdays={"Anika":"20/07/2007", "Jake":"09/07/2008","Jill":"03/03/2006"}

with open("birthdays.json","w") as b:
    json.dump(birthdays, b)


with open ("birthdays.json","r") as f:
    birthday=json.load(f)


print("Welcome to the birthday dictionary! We know the birthdays of :")
for key in birthday.keys():
    print(key)
request=input("Whose birthday would you like to know : ")
print(f"{request}'s birthday is on {birthday[request]}")