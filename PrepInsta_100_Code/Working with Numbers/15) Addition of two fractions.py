# Addition of two fractions
# First fraction consist of 1 as numerator and 3 as denominator, and Second fraction consist of 3 as numerator and 9 as denominator.

#  (1 / 3) + (3 / 9) = (6 / 9) = (2 / 3)

# Find LCM of 3 and 9 and the result will be 9.
# Multiply 3 in first fraction : (3 / 9) + (3 / 9)
# Add both fractions and then the result will be : (6 / 9)
# Now simplify it by finding the HCF of 6 and 9 and the result will be 3.
# So divide 6 and 9 by 3 and then the result will be : (2 / 3)

def addition_of_two_fraction(num1,deno1,num2,deno2):
    sol1 = (num1*deno2) + (num2*deno1)
    sol2 = (deno1*deno2)
    for i in range(1,min(sol1,sol2)+1):
        if(sol1%i==0 and sol2%i==0):
            sol1=sol1//i
            sol2=sol2//i
    print(sol1,"/",sol2)

num1=int(input())
deno1=int(input())
num2=int(input())
deno2=int(input())
addition_of_two_fraction(num1,deno1,num2,deno2)
