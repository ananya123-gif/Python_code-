# Find All Subsets

def subset(A,sub=[],idx=0):
    print(*sub)
    for i in range(idx,len(A)):
        sub.append(A[i])
        subset(A,sub,i+1)
        sub.pop(-1)
    return

arr=list(map(int,input().split(" ")))
subset(arr)
