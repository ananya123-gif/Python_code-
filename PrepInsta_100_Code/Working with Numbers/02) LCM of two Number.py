# LCM of two numbers
# Input : a=12 b=14
# Output : sol = 84

def solve(a,b):
    for i in range(1, max(a,b)):
        if a%i==b%i==0:
            hcf = i
    lcm = (a*b)//hcf
    return lcm

a,b=map(int,input().split())
print(solve(a,b))
