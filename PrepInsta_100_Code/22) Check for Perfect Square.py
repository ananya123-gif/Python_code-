# Check for Perfect Square
# We are given an integer number and need to print “True” if it is Perfect Square, otherwise “False”.

def perfect_square(num):
    for i in range(1,num+1):
        if(num%i==0):
            p=num//i
            if(p*p==num):
                print(num,"is Perfect Square")
                return
    print(num,"is not Perfect Square")

num=int(input())
perfect_square(num)
