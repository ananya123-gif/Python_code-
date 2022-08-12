# Number of digits in an integer

import math

def number_of_digits(num):
    n=str(num)
    n1 = len(n)                             #Method 1

    n2 = math.floor(math.log10(num)+1)      #Method 2

    print("By Method 1:",n1)
    print("By Method 2:",n2)

num=int(input())
number_of_digits(num)
