#Let's define a beautiful function f(x) in such a way: Add 1 to the value of x, if the result of addition
#contains any trailing zeros the remove them all.

#input = 1783

#1783 -> 1784,1785,1786,1787,1788,1789,1790 = 7    (10-7)
#179 --> 180                                = 1    (10-9)
#18  --> 19,20                              = 2    (10-8)
#2   --> 3,4,5,6,7,8,9,1,2                  = 9
#                                       Sum = 19

#Output = 19

def beautiful_fxn(n):
    s = 0
    num = str(n)
    i = len(num) - 1
    carry = 0
    while (i > 0):
        c_d = 10 - (int(num[i]) + carry)
        s = s + c_d
        carry = 1
        i -= 1
    s = s + 9
    return s

n = int(input("Give value = "))
x = beautiful_fxn(n)
print(x)
