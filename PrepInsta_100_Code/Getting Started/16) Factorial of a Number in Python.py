# Factorial of a Number in Python
# Here we will discuss how to find the Factorial of a Number in Python programming language.
# Factorial of any number is the product of it and all the positive numbers below it for example factorial of 5 is 120
# Factorial of n (n!) = 1 * 2 * 3 * 4....n

# 5! = 1 x 2 x 3 x 4 x 5 = 120
# 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return factorial(n-1)*n

n=int(input())
print(factorial(n))
