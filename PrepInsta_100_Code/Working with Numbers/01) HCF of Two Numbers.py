# HCF of Two Numbers
# HCF means (Highest Common Factor) also known as GCD (Greatest Common Divisor).

# x is called HCF of a & b two conditions :
# x can completely divide both a & b leaving remainder 0
# No, other number greater than x can completely divide both a & b

#Example:
#Input:  a = 36, b = 60
#Output: sol = 12

def hcf(a,b):
    hcf=0
    for i in range(1,min((a,b))):
        if(a%i==0 and b%i==0):
            hcf=i
    return hcf

a,b=map(int,input().split())
print(hcf(a,b))
