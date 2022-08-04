# Check Whether or Not the Number is a Palindrome.
# Given an integer number as an input, the objective is to check Whether or not the number is a palindrome.

# Example
# Input : 1221
# Output : Palindrome

def palindrome(num):
    p=str(num)
    if(str(num)==p[::-1]):
        print(num,"is Palindrome")
    else:
        print(num,"is not Palindrome")

num=int(input())
palindrome(num)
