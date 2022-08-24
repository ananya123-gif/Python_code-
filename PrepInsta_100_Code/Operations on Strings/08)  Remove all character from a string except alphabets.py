# Remove all character from a string except alphabets

# Input:  String = "#Justice!For@Chutki123"
# Output: JusticeForChutki

def remove_except_alpha(s):
    s1=''
    for i in s:
        if(i.isalpha()):
            s1+=i
    return s1

s=input()
print(remove_except_alpha(s))
