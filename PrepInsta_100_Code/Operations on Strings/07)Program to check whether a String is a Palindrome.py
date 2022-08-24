# Program to check whether a String is a Palindrome

# Input:  s='civic'
# Output: civic is Palindrome

def palindrome(s):
    if(s==s[::-1]):
        print(s,"is Palindrome")
    else:
        print(s,"is not palindrome")

s=input()
palindrome(s)
