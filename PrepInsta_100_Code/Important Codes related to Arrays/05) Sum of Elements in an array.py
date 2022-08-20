# Sum of Elements in an array

# Example

# Input:  arr = [10, 89, 9, 56, 4, 80, 8]
# Output: Sum is 256

def sum_of_element(arr):
    s=0
    for i in arr:
        s+=i
    return s

arr=list(map(int,input().split(" ")))
print("Sum is ",sum_of_element(arr))
