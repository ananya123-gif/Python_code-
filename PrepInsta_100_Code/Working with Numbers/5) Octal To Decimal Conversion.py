# Octal To Decimal Conversion
# Octal Number = 512
# Decimal Number = 330

def oct_to_dec(num):
    s=str(num)
    s=s[::-1]
    c=0
    for i in range(len(s)):
        c+=int(s[i])*pow(8,i)
    print(c)

num=int(input())
oct_to_dec(num)
