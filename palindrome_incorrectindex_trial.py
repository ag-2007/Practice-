word = input("Enter a word : ")
palindrome = False

for i in range(0,len(word)):
    if word[i]==word[len(word)-i] :
        palindrome = True
    else:
        palindrome=False

if palindrome == True:
    print("Yes it is a palindrome")
else:
    print("Sorry it's not a palindrome")

    
