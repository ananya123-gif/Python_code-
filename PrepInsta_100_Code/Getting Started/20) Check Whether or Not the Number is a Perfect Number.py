# Check Whether or Not the Number is a Perfect Number.
# Given an integer input as a number, the objective is to check whether or not a number is a Perfect Number.

# Example
# Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28

# Output : It's a Perfect Number

def perfect_number(num):
    s=0
    for i in range(1,num):
        if(num%i==0):
            s=s+i
    if(s==num):
        print(num,"is Perfect Number")
    else:
        print(num,"is not Perfect Number")

num=int(input())
perfect_number(num)
