# Input the string
string = input('Enter a string: ')

# Empty string to for stroring reverserd string
reversed_string = ''

i = len(string)

# Using while loop to go back
while i > 0:
    i = i - 1
    reversed_string += string[i]

    # Print the reversed string
    print('reversed string: ', reversed_string)
