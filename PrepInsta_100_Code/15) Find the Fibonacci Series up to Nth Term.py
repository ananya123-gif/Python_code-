# Find the Fibonacci Series up to Nth Term.
# Given an integer as an input, the objective is to find the Fibonacci series until the number input as the Nth term.
#
# Example
# Input : 4
# Output : 0 1 1 2

def fibonacci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_series(n):
    for i in range(1,n+1):
        print(fibonacci(i),end=" ")

n=int(input())
fibonacci_series(n)
