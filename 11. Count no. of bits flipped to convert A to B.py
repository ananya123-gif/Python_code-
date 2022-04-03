# Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’. 
# Example : 
 
# Input : a = 10, b = 20
# Output : 4
# Binary representation of a is 00001010
# Binary representation of b is 00010100
# We need to flip highlighted four bits in a
# to make it b.

# Input : a = 7, b = 10
# Output : 3
# Binary representation of a is 00000111
# Binary representation of b is 00001010
# We need to flip highlighted three bits in a
# to make it b.

def countFlips(a,b):
    c=0
    while(a>0 or b>0):
        p=(a&1)
        q=(b&1)
        if(p!=q):
            c+=1
        a>>=1
        b>>=1
    return c

a=10
b=20
print(countFlips(a,b))
