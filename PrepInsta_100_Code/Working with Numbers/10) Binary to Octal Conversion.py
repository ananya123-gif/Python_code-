# Binary to Octal Conversion
# Input:  1010
# Output: 12

def bin_to_oct(num):
    s = str(num)
    s = s[::-1]
    c = 0
    for i in range(len(s)):
        c += int(s[i]) * pow(2, i)
    n=int(c)
    s1 = ''
    while (n != 0):
        r = n % 8
        s1 = s1 + str(r)
        n = n // 8
    print(int(s1[::-1]))

num=int(input())
bin_to_oct(num)
