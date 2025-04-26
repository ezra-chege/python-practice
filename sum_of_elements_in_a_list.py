# Sum of numbers in a lsit using recursion

def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
    
numbers = [1, 2, 3]

print( sum_list(numbers) )