def fibonacci (n):
    fibonacci_nums=[1,1]
    for x in range (n-2):
        new = int(fibonacci_nums[-1])+ int(fibonacci_nums[-2])
        fibonacci_nums.append(new)
    return (fibonacci_nums)

fibonacci_numbers = int(input("Enter how many fibonnaci numbers you want : "))
final = fibonacci(fibonacci_numbers)
print(final)
