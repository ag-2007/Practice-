name=input("Hello, Please enter your name : ")
print("Wonderful, now enter your age and let me tell you the year you will turn a 100 in a text file nearby")
age= int(input())
year=2023+(100-age)

file_path = 'D:/Anika Gupta/Others/IAMNEO/Coding/Practice python/Exercises/write_to_file/file_to_save.txt'
with open(file_path, 'w') as open_file:
    open_file.write("So "+ name + " ,you will turn 100 in the year " + str(year))
    

## This helped
    ##import os

##current_directory = os.getcwd()
##print("Current Working Directory:", current_directory)
    