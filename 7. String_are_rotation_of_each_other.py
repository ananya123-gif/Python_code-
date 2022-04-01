# Given a string s1 and a string s2,
# write a snippet to say whether s2 is a rotation of s1?
# (eg given s1 = ABCD and s2 = CDAB, return true,
# given s1 = ABCD, and s2 = ACBD , return false)

def rotation(s1,s2):
    if(len(s1)!=len(s2)):
        return 0
    temp=s1+s1
    if(temp.count(s2)>0):
        return True
    else:
        return False

s1 = "ABCD"
s2 = "CDAB"
if rotation(s1,s2):
    print("Strings are rotation of each other.")
else:
    print("Strings are not rotation of each other.")
