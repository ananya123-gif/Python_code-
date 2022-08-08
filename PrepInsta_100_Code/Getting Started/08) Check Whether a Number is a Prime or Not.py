# Check Whether a Number is a Prime or Not.
# Given an integer input the objective is to write a program to Check Whether a Number is a Prime or Not.

# Example
# Input : 11
# Output : 11 is a Prime

def prime(num):
    if(num<=1):
        print(num,"is Not Prime")
    else:
        c=0
        for i in range(1,num+1):
            if(num%i==0):
                c+=1
        if(c==2):
            print(num,"is Prime")
        else:
            print(num,"is not Prime")

num=int(input())
prime(num)
