# Given an array arr[] consisting of N integers which are either 0 or 7, 
# the task is to find the largest number that can be formed using the array elements such that it is divisible by 50.

# Examples:
  
# Input: arr[] = {7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0}
# Output: 777770000000

# Input: arr[] = {7, 0}
# Output: 0

def largest(arr):
    arr.sort()
    arr.reverse()
    s=""
    for i in range(len(arr)):
        s+=str(arr[i])
    s=int(s)
    if(s%50==0):
        return s
    else:
        return 0

arr=[7,0]
print(largest(arr))
