# Removing Duplicates elements from an array

# Example

# Input : arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
# Output : 10 20 30 40 50

def remove_dup(arr):
    for i in arr:
        if(arr.count(i)>1):
            arr.remove(i)
    return arr

arr = list(map(int,input().split()))
print(*remove_dup(arr))
