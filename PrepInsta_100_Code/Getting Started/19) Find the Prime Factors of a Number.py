# Find the Prime Factors of a Number.
# Given an integer input as the number, the objective is to Find all the Prime Factors of a the given integer input number.

# Example
# Input : 210
# Output : 2 3 5 7

def prime(num):
    if(num<=1):
        return 0
    else:
        c=0
        for i in range(1,num+1):
            if(num%i==0):
                c+=1
        if(c==2):
            return 1
        else:
            return 0

def factor(num):
    for i in range(2,num):
        if(num%i==0 and prime(i)):
            print(i,end=" ")

num=int(input())
factor(num)
