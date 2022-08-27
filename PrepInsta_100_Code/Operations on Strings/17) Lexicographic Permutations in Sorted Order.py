# Lexicographic Permutations in Sorted Order
# Input:  "ABC"
# Output: ABC, ACB, BAC, BCA, CAB, CBA

ans=[]
def permute(a,l,r):
    if(l==r):
        ans.append(''.join(a))
    else:
        for i in range(l,r):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]
    return ans

a=input()
a=list(a)
print(*permute(a,0,len(a)))
