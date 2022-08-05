# Check Whether or Not the Two Numbers  are Friendly Pairs.
# Given two integer numbers as the input, the objective is to check whether or not the two numbers are Friendly pairs of each other.

# Example
# Input : 6 28
# Output : Yes, they are a friendly pair
# Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively.
# When we divide the sums with the numbers we get 1 and 1 respectively.
# As the ratio of both the number match, they are considered as a friendly pair.

def friendly_pair(a,b):
    s1=0
    s2=0
    for i in range(1,a):
        if(a%i==0):
            s1+=i
    for j in range(1,b):
        if(b%j==0):
            s2+=j
    if(s1==a and s2==b):
        print(a,"and",b,"are Friendly Pair")
    else:
        print(a,"and",b,"are not Friendly Pair")

a,b=map(int,input().split())
friendly_pair(a,b)
