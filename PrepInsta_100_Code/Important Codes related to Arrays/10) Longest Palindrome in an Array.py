# Longest Palindrome in an Array

# Input:  arr = [1, 232, 5545455, 909090, 161]
# Output: 5545455

def longest_palin(arr):
    l=[]
    m=0
    for i in arr:
        p=str(i)
        if(m<len(p) and p[::-1]==str(i)):
            m=len(p)
            l.append(p)
    return int(l[-1])

arr = [1, 232, 5545455, 909090, 161]
print(longest_palin(arr))
