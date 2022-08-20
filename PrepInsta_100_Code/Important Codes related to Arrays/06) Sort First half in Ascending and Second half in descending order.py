# Sort First half in Ascending and Second half in descending order

# Input : arr = [1, 90, 34, 89, 7, 9]
# Output : 1 7 9 90 89 34

def asc_dec(arr):
    mid=len(arr)//2
    arr.sort()
    arr1=arr[:mid]
    arr2=arr[mid:][::-1]
    arr=arr1+arr2
    return arr

arr=[1,90,34,89,7,9]
print(*asc_dec(arr))
