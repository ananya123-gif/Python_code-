# Find Prime number between 1 to 100

def prime(num):
    if(num<=1):
        return False
    else:
        c=0
        for i in range(1,num+1):
            if(num%i==0):
                c+=1
        if(c==2):
            return True
        else:
            return False

def solve():
    for j in range(1,101):
        if(prime(j)):
            print(j,end=" ")

solve()
