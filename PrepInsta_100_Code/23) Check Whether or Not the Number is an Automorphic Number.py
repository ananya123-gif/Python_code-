# Check Whether or Not the Number is an Automorphic Number
# Given an integer input for a number, the objective is to check whether or not the number is Automorphic or not.

# Input : number = 5
# Output : It's an Automorphic number.
# Explanation : Number = 5
# Square of number = 25
# as the square of the number ends with the number itself, It's an Automorphic number.

# Example
# Input : 5
# Output : It's an Automorphic Number.

def automorphic(num):
    p=num*num
    s=str(p)
    s=s[::-1]
    r=len(str(num))
    t=s[:r]
    if(t==str(num)):
        print(num,"is an Automorphic Number")
    else:
        print(num,"is not Automorphic Number")

num=int(input())
automorphic(num)
