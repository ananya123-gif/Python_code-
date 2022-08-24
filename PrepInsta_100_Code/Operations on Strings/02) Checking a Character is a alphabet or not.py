# Checking a Character is a alphabet or not

# Input:  c ='f'
# Output: f is alphabet

def check_alpha(c):
    if(c>='a' and c<='z' or c>='A' and c<='Z'):
        print(c,"is alphabet")
    else:
        print(c,"is not alphabet")

c=input("Enter a character : ")
check_alpha(c)
