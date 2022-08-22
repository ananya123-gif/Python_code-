# Find maximum product sub-array in a given array

# Example
# Input : arr = [ 1, -2, -3, 0, 7, -8, -2 ]
# Output : Maximum product sub-array is 112

def max_prod_sub(arr):
    res=arr[0]
    for i in range(len(arr)):
        mul=arr[i]
        for j in range(i+1,len(arr)):
            res=max(res,mul)
            mul*=arr[j]
        res=max(res,mul)
    return res

arr=list(map(int,input().split()))
print(max_prod_sub(arr))
