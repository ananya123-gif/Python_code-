# Power of a Number using Recursion

def power(base,po):
    if(po==0):
        return 1
    else:
        return power(base,po-1)*base

base=int(input())
po=int(input())
print(power(base,po))
