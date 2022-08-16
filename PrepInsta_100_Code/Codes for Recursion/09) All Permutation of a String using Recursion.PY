# All Permutation of a String using Recursion

def swap(a,b):
    t=a
    a=b
    b=t

def permute(s,l,r):
    if(l==r):
        print(s,end=" ")
    else:
        for i in range(l,r+1):
            swap(s[l],s[i])
            permute(s,l+1,r)
            swap(s[l],s[i])

s=input()
r=len(s)
permute(s,0,r-1)
