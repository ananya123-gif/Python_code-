# Finding Repeating elements in an Array

# Example
# Input : arr = [10, 20, 40, 30, 50, 20, 10, 20]
# Output : 10 20

# Explanation : 40, 30 and 50 are occur 1 time in the given array, 10 occurs 2 times and 20 occurs 3 times

def repeat_ele(arr):
    l=[]
    for i in arr:
        if(arr.count(i)>1 and (i not in l)):
            l.append(i)
    return l

arr = list(map(int,input().split()))
print(*repeat_ele(arr))
