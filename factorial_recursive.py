# Calculating the factorial using recursion

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
# Input a non-negative number
number = int(input("Enter a non-negative integer to calculate its factorial: "))

# print the factorial
print(f"The factorial of {number} is {factorial_recursive(number)}")
