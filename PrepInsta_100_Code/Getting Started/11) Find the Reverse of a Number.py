# Find the Reverse of a Number.
# Given an integer input the objective is to reverse the given integer number using loops and slicing.

# Example
# Input : 123
# Output : 321

def reverse(num):
    return str(num)[::-1]

num=int(input())
print(reverse(num))
