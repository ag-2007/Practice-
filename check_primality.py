def check_primality(num):
    divisors = []

    for element in range (1,num+1):
        if num % element == 0:
            divisors.append(element)
    
    if len(divisors)==2:
        return True
    else:
        return False


usr_inp = int(input("Enter a number for which you wish to see the primality of : "))
check = check_primality(usr_inp)
if check == True:
    print("Yes it is a prime number")
else:
    print("No it is not a prime number")


        
        

