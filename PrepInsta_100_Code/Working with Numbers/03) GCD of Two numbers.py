# GCD of Two numbers.
# Basically, the GCD (Greatest Common Divisor) or HCF (highest common factor ) of two numbers
# is the largest positive integer that divides each of the integers where the user entered number should not be zero.

#Input: a=60, b=48
#Output: sol=12

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


a,b=map(int,input().split())
print(gcd(a,b))
