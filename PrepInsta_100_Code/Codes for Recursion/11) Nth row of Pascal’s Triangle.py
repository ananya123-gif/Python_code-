# Nth row of Pascal’s Triangle

#         1
#        1 1
#       1 2 1
#      1 3 3 1
#     1 4 6 4 1
# 4C0  4C1 4C2 4C3 4C1

# Input:  3
# Output: 1 3 3 1

def getrow(n):
    p=1
    print(p,end=" ")
    for i in range(1,n+1):
        c=(p*(n-i+1))//i
        print(c,end=" ")
        p=c

n=int(input())
getrow(n)
