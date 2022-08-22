# Find non-repeating elements in an array

# Example

# Input : arr[8] = [10, 20, 70, 90, 80, 20, 10, 20]
# Output : 70 90 80
# Explanation : 70, 90 and 80 are occur 1 time in the given array, 10 occurs 2 times and 20 occurs 3 times.

def non_repeat_ele(arr):
    l=[]
    for i in arr:
        if(arr.count(i)==1 and (i not in l)):
            l.append(i)
    return l

arr = list(map(int,input().split()))
print(*non_repeat_ele(arr))
