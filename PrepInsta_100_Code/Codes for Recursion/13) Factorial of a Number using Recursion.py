# Factorial of a Number using Recursion

# Input:  5
# Output: 120

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

n=int(input())
print(factorial(n))
