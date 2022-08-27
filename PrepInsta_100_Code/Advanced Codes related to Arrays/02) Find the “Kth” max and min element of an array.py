# Find the “Kth” max and min element of an array

# Input: array=  [1, 7, 6, 8, 9, 2, 4, 5, 3, 0] ,  k = 2
# Output: kth largest element:  8
#         kth smallest element: 1

def max_min_ele(arr,k):
    arr.sort()
    print("kth largest element:",arr[len(arr)-k])
    print("kth smallest element:",arr[k-1])

arr=list(map(int,input().split()))
k=int(input())
max_min_ele(arr,k)
