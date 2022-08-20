# Smallest and Largest Element in an array

# Example:

# Input:  arr = [10, 89, 9, 56, 4, 80, 8]
# Output: Smallest Element is 4
#         Largest Element is 89

def smallest_largest(arr):
    arr.sort()
    print("Smallest Element is ",arr[0])
    print("Largest Element is ",arr[-1])

arr=list(map(int,input().split(" ")))
smallest_largest(arr)
