# Find the Armstrong Number in a given Range.
# Given two integers high and low for limits as inputs,
# the objective is to write a code to Find the Armstrong Numbers in a given Interval.

# For Instance,
# Input : 150 160
# Output : 153

def armstrong(num):
    p=num
    n=len(str(p))
    s=0
    while(num!=0):
        r=num%10
        s=s+pow(r,n)
        num=num//10
    if(s==p):
        return 1
    else:
        return 0

def armstrong_num_range(low,high):
    for i in range(low,high+1):
        if(armstrong(i)):
            print(i,end=" ")

low,high=map(int,input().split())
armstrong_num_range(low,high)
