# N-bit binary numbers having more  or equal 1’s than 0’s

# Example :

# Input : 4
# Output : 1111 1110 1101 1100 1011 1010
# Explanation : 1111 1110 1101 1100 1011 1010 all these are the required binary numbers

def printrec(num,extra_1,rem_place):
    if(0==rem_place):
        print(num,end=" ")
        return
    printrec(num+"1",extra_1+1,rem_place-1)
    if(0<extra_1):
        printrec(num+"0",extra_1-1,rem_place-1)

def primenums(n):
    str=""
    printrec(str,0,n)

n=int(input())
primenums(n)
