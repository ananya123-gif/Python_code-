# Find Maximum Scalar Product of Two Vectors in an Array

# Input :     arr1 = [10, 30, 40, 20]
#             arr2 = [2, 4, 5, 1]

# Output : 370
# Explanation : 10*1 + 20*2 + 30*4 + 40*5 = 370

def max_scalar_prod(arr1,arr2):
    arr1.sort()
    arr2.sort()
    prod=0
    for i in range(len(arr1)):
        prod+=(arr1[i]*arr2[i])
    return prod

arr1 = list(map(int,input("Enter elements in aar1 : ").split(" ")))
arr2 = list(map(int,input("Enter elements in aar2 : ").split(" ")))
print(max_scalar_prod(arr1,arr2))
