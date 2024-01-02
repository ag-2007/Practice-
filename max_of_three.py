def max_finder(a:int,b:int,c:int):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return("No repeated terms, sorry")
    
numbers=input("Enter three numbers in the form a b c : ")
num=list(map(int,numbers.strip().split()))
print(max_finder(num[0],num[1],num[2]))
