# Octal To Binary Conversion
# Input:  12
# Output: 1010

def oct_to_bin(num):
    s = str(num)
    s = s[::-1]
    c = 0
    for i in range(len(s)):
        c += int(s[i]) * pow(8, i)
    n=c
    s1 = ''
    while (n != 0):
        r = n % 2
        s1 = s1 + str(r)
        n = n // 2
    print(int(s1[::-1]))

num=int(input())
oct_to_bin(num)
