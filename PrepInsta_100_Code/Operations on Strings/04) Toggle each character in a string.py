# Toggle each character in a string

# Input:  String = 'GuDDuBHaiyA'
# Output: gUddUbhAIYa

def toggle(s):
    s1=''
    for i in s:
        if i.isupper():
            s1+=i.lower()
        elif i.islower():
            s1+=i.upper()
    return s1

s=input("Enter string: ")
print(toggle(s))
