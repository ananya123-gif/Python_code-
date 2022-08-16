# Sums of all Subsets

def subset(arr,l,r,sum):
    if(l>r):
        print(sum,end=" ")
        return
    subset(arr,l+1,r,sum+arr[l])
    subset(arr,l+1,r,sum)

arr=list(map(int,input().split()))
n=len(arr)
subset(arr,0,n-1,0)
