# Binary to Decimal Conversion
# Binary Number = 10
# Decimal Number = 2

def bin_to_dec(num):
    s=str(num)
    s=s[::-1]
    c=0
    for i in range(len(s)):
        c+=int(s[i])*pow(2,i)
    print(c)

num=10
bin_to_dec(num)
