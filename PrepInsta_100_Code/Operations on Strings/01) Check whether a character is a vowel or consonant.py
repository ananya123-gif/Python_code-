# Checking a Character is a vowel or consonant

# Input:  c ='f'
# Output: f is a consonant

def check_vowel_or_cons(c):
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or
       c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
        print(c,"is Vowel")
    else:
        print(c,"is Consonant")

c=input("Enter a character : ")
check_vowel_or_cons(c)
