# Largest Element in an Array
# Given an array of integers “A”, the task is to write a Program for Finding the Largest Element
# in an Array using recursion algorithm.

# Input: A = [1, 4, 3, -5, -4, 8, 6]
# Output: 8

def largest_element(A,n):
    if(n==1):
        return A[0]
    else:
        return max(A[n-1],largest_element(A,n-1))

A=list(map(int,input().split()))
n=len(A)
print(largest_element(A,n))
