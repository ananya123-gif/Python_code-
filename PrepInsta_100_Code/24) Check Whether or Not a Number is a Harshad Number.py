# Check Whether or Not a Number is a Harshad Number.
# Given an integer input the objective is to check whether or not the given number is a Harshad Number or not.
# To do so we’ll check if the sum of the digits can perfectly divide the number or not.

# Example
# Input : 21
# Output : Yes It's a Harshad Number  (2 + 1 = 3) 21 is divisible by 3.

def harshad_number(num):
    p=num
    s=0
    while(num!=0):
        s+=num%10
        num=num//10
    if(p%s==0):
        print(p,"is Harshad Number")
    else:
        print(p,"is not Harshad Number")

num=int(input())
harshad_number(num)
