# Find whether arrays or disjoint or not
#
# Input:  array1 1 2 3 4 5
#         array2 4 5 6 7 8
#
# Output: Not disjoint

def array_disjoint(arr1,arr2):
    for i in arr1:
        if i in arr2:
            print("Not disjoint")
            return
    print("Disjoint")

arr1= list(map(int,input().split()))
arr2= list(map(int,input().split()))
array_disjoint(arr1,arr2)
