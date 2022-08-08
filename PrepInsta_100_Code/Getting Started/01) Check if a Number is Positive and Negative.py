#Check if a Number is Positive and Negative.
def positive_or_negative(num):
    if(num>0):
        print(num," is Positive")
    elif(num<0):
        print(num," is Negative")
    else:
        print("Zero")

num=int(input())
positive_or_negative(num)
