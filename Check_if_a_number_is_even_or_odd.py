def is_even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n - 2)

# input from the user
number = int(input("Enter a number: "))

if is_even(number):
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
