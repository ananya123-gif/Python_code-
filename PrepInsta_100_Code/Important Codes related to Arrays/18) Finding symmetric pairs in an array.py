# Finding symmetric pairs in an array

# Example

# Input : arr[5][2] = {{10,20}, {30,40}, {50,60}, {20,10}, {40,30}, {90, 100}, {1, 9}, {100, 90}}
# Output : (10,20) (30,40) (90, 100)

def find_symmetric(arr):
    l=[]
    for i in arr:
        if i[::-1] in arr and (i[::-1] not in l):
            l.append(i)
    return l

arr=[[10,20],[30,40],[50,60],[20,10],[40,30],[90,100],[1,9],[100,90]]
print(*find_symmetric(arr))
