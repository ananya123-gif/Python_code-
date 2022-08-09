# For Permutations In Which N People Can Occupy R Seats In A Classroom
# Input:  10, 6
# Output: 151200

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return factorial(n-1)*n

def permutation(n,r):
    sol=factorial(n)//factorial(n-r)
    return sol

n,r=map(int,input().split())
print(permutation(n,r))
