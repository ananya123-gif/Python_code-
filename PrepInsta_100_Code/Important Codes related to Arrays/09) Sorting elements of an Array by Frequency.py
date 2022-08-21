# Sorting elements of an Array by Frequency
# Input:  [10, 20, 30, 40, 40, 50, 50, 50]
# Output: [50, 50, 50, 40, 40, 10, 20, 30]

def sorting_ele(arr):
    l=[]
    for i in arr:
        if [arr.count(i),i] in l:
            pass
        else:
            l.append([arr.count(i),i])
    l.sort(reverse=True)
    sol=[]
    for j in l:
        if(j[0]!=1):
            while(j[0]!=0):
                sol.append(j[-1])
                j[0]-=1
    l.sort()
    for j in l:
        if(j[0]==1):
            sol.append(j[-1])
    return sol

arr=[10,20,30,40,40,50,50,50]
print(sorting_ele(arr))
