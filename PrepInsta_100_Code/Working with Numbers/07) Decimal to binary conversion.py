# Decimal to binary conversion
# Input:  4
# Output: 100

def dec_to_bin(num):
    s=''
    while(num!=0):
        r=num%2
        s=s+str(r)
        num=num//2
    print(int(s[::-1]))

num=int(input())
dec_to_bin(num)
