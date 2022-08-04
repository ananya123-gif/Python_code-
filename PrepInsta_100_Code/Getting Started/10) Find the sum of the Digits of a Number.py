# Find the sum of the Digits of a Number.
# Given an input the objective to find the Sum of Digits of a Number.
# To do so we’ll first extract the last element of the number and then keep shortening the number itself.

# Example
# Input : number = 123
# Output : 6

def sum_of_digits(num):
    s=0
    while(num!=0):
        s+=num%10
        num=num//10
    return s

num=int(input())
print(sum_of_digits(num))
