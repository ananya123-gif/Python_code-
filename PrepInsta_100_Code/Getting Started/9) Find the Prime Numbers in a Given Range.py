# Find the Prime Numbers in a Given Range.
# Given two integer as Limits, low and high, the objective is to write a code to Find Prime Numbers in a Given Range.

# Example
# Input : low = 2 , high = 10
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

def prime_number_range(low,high):
    for i in range(low,high+1):
        if(prime(i)):
            print(i,end=" ")

low=int(input())
high=int(input())
prime_number_range(low,high)
