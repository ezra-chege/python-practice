# python-practice

## Sum List Using Recursion

A simple Python script to find the sum of numbers in a list using recursion.

## Code

```python
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

numbers = [1, 2, 3]
print(sum_list(numbers))  # Output: 6