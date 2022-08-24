# Remove brackets from an algebraic expression

# Input: (x+y)+(z+q)
# Output: x+y+z+q

def remove_brac(s):
    s1=''
    l=['(',')','{','}','[',']']
    for i in s:
        if(i not in l):
            s1+=i
    return s1

s=input()
print(remove_brac(s))
