# Find Non Repeating Characters

# Input:  String = "prepinsta"
# Output: r e i n s t a

def find_non_repeat(s):
    l=[]
    for i in s:
        if i in l:
            pass
        else:
            l.append(i)
    return l

s=input("Enter String : ")
print(find_non_repeat(s))
