# Write your code here :-)
print ('type a number')
x=input()

while x != 1:
    if int(x) % 2==0:
     x = int(x) / 2
     print (x)
    else:
     x= 3 * int(x) + 1
     print (x)
