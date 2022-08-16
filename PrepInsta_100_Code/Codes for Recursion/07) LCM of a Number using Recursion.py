# LCM of a Number using Recursion

def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b,a%b)

def lcm(a,b):
    return (a*b)//hcf(a,b)

a=int(input())
b=int(input())
print(lcm(a,b))
