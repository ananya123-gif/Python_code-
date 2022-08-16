# HCF of a Number using Recursion

def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b,a%b)

a=int(input())
b=int(input())
print(hcf(a,b))
