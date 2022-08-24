# Program to remove the vowels

# Input:  string = PrepInsta
# Output: Prpnst

def remove_vowel(s):
    s1=''
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or
           i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            pass
        else:
            s1+=i
    return s1

s=input("Enter String :")
print(remove_vowel(s))
