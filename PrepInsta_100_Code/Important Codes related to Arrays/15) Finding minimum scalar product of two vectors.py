# Finding minimum scalar product of two vectors

# Input:  arr1 = [1, 2, 6, 3, 7]
#         arr2 = [10, 7, 45, 3, 7]

# Output: 149

def min_scalar_prod(arr1,arr2):
    arr1.sort()
    arr2.sort(reverse=True)
    prod=0
    for i in range(len(arr1)):
        prod+=(arr1[i]*arr2[i])
    return prod

arr1 = list(map(int,input("Enter elements in aar1 : ").split(" ")))
arr2 = list(map(int,input("Enter elements in aar2 : ").split(" ")))
print(min_scalar_prod(arr1,arr2))
