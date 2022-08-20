# Second Smallest Element in an array

# Example:

# Input:  arr = [10, 89, 9, 56, 4, 80, 8]
# Output: Second Smallest Element is 8

def smallest_largest(arr):
    arr.sort()
    print("Second Smallest Element is",arr[1])

arr=list(map(int,input().split(" ")))
smallest_largest(arr)
