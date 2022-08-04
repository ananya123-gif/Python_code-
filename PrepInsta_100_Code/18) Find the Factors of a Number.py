# Find the Factors of a Number.
# Given an integer Number as input, the objective is to search for all the factors of the Given integer input.

# Example
# Input : 10
# Output : 2 5

def factor(num):
    for i in range(2,num):
        if(num%i==0):
            print(i,end=" ")

num=int(input())
factor(num)
