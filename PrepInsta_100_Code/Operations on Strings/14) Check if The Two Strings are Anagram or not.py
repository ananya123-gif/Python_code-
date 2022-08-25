# Check if The Two Strings are Anagram or not

# Input:  s1="SILENT"
#         s2="LISTEN"
# Output: s1 and s2 are Anagram

def anagram(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    if(s1==s2):
        print("s1 and s2 are Anagram")
    else:
        print("s1 and s2 are not Anagram")

s1=input("Enter first String: ")
s2=input("Enter second String: ")
anagram(s1,s2)
