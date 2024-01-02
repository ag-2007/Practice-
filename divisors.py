num = int(input("Enter a number for which you want the divisors of : "))
x = range(1,num+1)
divisors = []

for element in x :
    if num % element == 0:
        divisors.append(element)

print(divisors)