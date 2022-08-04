# Strong number
# In this program we will find whether a number is strong number.
# A Strong Number is a number whose sum of factorial digits is equal to the number itself.

# Ex:- number is 145
# 1! + 4! + 5! = 145
# So it is a strong number.

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return factorial(n-1)*n

def strong_number(num):
    s=0
    p=num
    while(num!=0):
        r=num%10
        s=s+factorial(r)
        num=num//10
    if(s==p):
        print(p,"is Strong Number")
    else:
        print(p,"is not Strong Number")

num=int(input())
strong_number(num)
