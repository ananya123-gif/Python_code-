# Array is a subset of another array

# Input:  array1 1 2 3 4 5
#         array2 1 2 5

# Output: Arr2 is subset of Arr1

def array_subset(arr1,arr2):
    c=0
    for i in arr1:
        if i in arr2:
            c+=1
    if(c==len(arr2)):
        print("Arr2 is subset of Arr1")

arr1= list(map(int,input().split()))
arr2= list(map(int,input().split()))
array_subset(arr1,arr2)
