#Check Whether a Number is Even or Odd in Python
def even_or_odd(num):
    if(num%2==0):
        print(num,"is Even")
    else:
        print(num,"is Odd")

num=int(input())
even_or_odd(num)
