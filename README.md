# Ezra Chege, 189924

# Factorial Calculator

This Python program calculates the factorial of a non-negative integer entered by the user.  
It uses a for loop to compute the factorial step-by-step.

## How It Works

1. The program prompts the user to input a non-negative integer.
2. It calculates the factorial by multiplying all integers from `1` up to the entered number.
3. It then prints the final result.


# Factorial Calculator Using Recursion

This Python program calculates the factorial of a non-negative integer entered by the user using recursion.

## How It Works

1. The program prompts the user to input a non-negative integer.
2. It calculates the factorial using a recursive function.
3. It then prints the final result.

## Recursive Factorial Formula:
The factorial of `n` is calculated using the following recursive formula:
n! = n × (n-1)! (for n > 1)


# Reverse String without inbuilt methods

This Python program takes a string input from the user and reverses it using a **while loop**.

## How It Works

1. The program prompts the user to input a string.
2. It then reverses the string character by character using a **while loop**.
3. It prints the reversed string.

## Example

If the user enters `"hello"`, the program will calculate the reverse and print olleh



# Sum of Digits Using Recursion

This Python program calculates the sum of digits of a given number using recursion.

## How It Works

1. The program prompts the user to input a number.
2. It calculates the sum of the digits by recursively extracting each digit from the number.
3. It prints the final result.

## Recursive Sum Formula:
The sum of digits of n is calculated using the recursive formula:
sum_of_digits(n) = (n % 10) + sum_of_digits(n // 10) (for n > 0)


# Sum of Numbers in a List Using Recursion

This Python program calculates the sum of numbers in a list using recursion.

## How It Works

1. The program defines a recursive function to sum the elements in a list.
2. The base case checks if the list is empty; if it is, it returns `0`.
3. If the list is not empty, the function adds the first element to the sum of the rest of the list, computed recursively.
4. It prints the final result.

## Example

If the user enters the list `[1, 2, 3]`, the program will calculate the sum:
1 + 2 + 3 = 6


# Check Whether a Number is Even or Odd Using Recursion

This Python program checks whether a given number is even or odd using recursion.

## How It Works

1. The program defines a recursive function that checks if a number is even or odd by reducing the number by `2` at each recursive step.
2. The base case is when the number is `0` (even) or `1` (odd).
3. It prints whether the number is even or odd based on the result of the recursive function.

### Recursive Logic:
 If n == 0, the number is even.
 If n == 1 , the number is odd.
 For any other number, the function recursively calls itself with `n - 2`.

## Example

If the user enters `4`, the program will calculate: 4 is even
If the user enters `7`, the program will calculate: 7 iss odd












