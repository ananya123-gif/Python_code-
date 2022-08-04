# Check Whether a Given Number is an Armstrong Number or Not.
# For a given integer the objective is to check whether or not the given integer is an Armstrong number or not.

# Example
# Input : 371
# Output : It's an Armstrong Number (3^3 + 7^3 + 1^3 = 371)

def armstrong(num):
    p=num
    n=len(str(p))
    s=0
    while(num!=0):
        r=num%10
        s=s+pow(r,n)
        num=num//10
    if(s==p):
        print(p,"is Armstrong Number")
    else:
        print(p,"is not Armstrong Number")

num=int(input())
armstrong(num)
