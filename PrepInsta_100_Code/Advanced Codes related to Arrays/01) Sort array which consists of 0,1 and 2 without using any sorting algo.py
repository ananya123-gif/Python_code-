# Sort array which consists of 0,1 and 2 without using any sorting algo

# Input: Array: 1 2 0 2 1 0 2 1 0 2 0 1
#Output: Array after sorting: 0 0 0 0 1 1 1 1 2 2 2 2

def sort_0_1_2(arr):
    sol=[]
    count_0=arr.count(0)
    count_1=arr.count(1)
    count_2=arr.count(2)
    for i in range(count_0):
        sol.append(0)
    for i in range(count_1):
        sol.append(1)
    for i in range(count_2):
        sol.append(2)
    return sol

arr=list(map(int,input("Array : ").split()))
print("Array after Sorting : ",*sort_0_1_2(arr))
