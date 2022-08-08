# Decimal to Octal conversion
# Input:  148
# Output: 224

def dec_to_oct(num):
    s=''
    while(num!=0):
        r=num%8
        s=s+str(r)
        num=num//8
    print(int(s[::-1]))

num=int(input())
dec_to_oct(num)
