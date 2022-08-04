# Check Whether or Not the Number is an Abundant Number.
# Given an integer input as the number, the objective is to check whether or the given integer number is an Abundant Number or not.

# Example
# Input : Number = 12
# Output : Yes, It's an Abundant Number
# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.

def abundant_number(num):
    s=0
    for i in range(1,num):
        if(num%i==0):
            s+=i
    if(s>num):
        print(num,"is Abundant Number")
    else:
        print(num,"is not Abundant Number")

num=int(input())
abundant_number(num)
