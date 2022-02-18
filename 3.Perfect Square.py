#Given a number N. Write a program to check whether it is a perfect number or not.
#Perfect Number is defined as the number whose sum of the factor gives the original number.
#If the number is a perfect number print "Yes" or "No".


def perfect_num(n):
    s = 1
    i = 2
    while ((i * i <= n)):
        if (n % i == 0):
            s = s + i + n / i
        i += 1
    if (s == n):
        return ("Yes")
    else:
        return ("No")

n = int(input())
x = perfect_num(n)
print(x)

