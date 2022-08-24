# Count the number of vowels in a string

# Input:  string = PrepInsta
# Output: Total vowels are :3

def count_num_vowel(s):
    c=0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or
           i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            c+=1
    return c

s=input("Enter String :")
print("Total vowels are :",count_num_vowel(s))
