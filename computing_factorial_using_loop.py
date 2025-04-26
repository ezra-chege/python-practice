# Input a number
number = int(input("Enter a non-negative integer: "))

# Initialize to 1
result = 1

# Multiply result by each number from 1 up to the input number
for i in range(1, number + 1):
    result *= i

# Print the factorial
print(f"The factorial of {number} is {result}")
