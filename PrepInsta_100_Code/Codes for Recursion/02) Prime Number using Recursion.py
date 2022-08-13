# Prime Number using Recursion

def prime(num,i=2):
    if(num==i):
        return True
    elif(num%i==0):
        return False
    return prime(num,i+1)

num=int(input())
print(prime(num))
