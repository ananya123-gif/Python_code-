# Find the Power of a Number.
# Given two integer input numbers, the objective is to find the power of the number raise to the power variable.

# Example
# Input : 2 3
# Output : 8

def power(a,b):
    m=1
    for i in range(b):
        m=a*m
    return m

a,b=map(int,input().split(" "))
print(power(a,b))
