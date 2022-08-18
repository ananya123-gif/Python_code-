# Smallest Element in an array

# Input : a = [10, 89, 9, 56, 4, 80, 8]
# Output : 4

def smallest_ele(a):
    s1=min(a)
    m=a[0]
    for i in range(len(a)):
        if(a[i]<m):
            m=a[i]
    s2=m
    print("By using direct function min",s1)
    print("By loop",s2)

a=list(map(int,input().split(" ")))
smallest_ele(a)
