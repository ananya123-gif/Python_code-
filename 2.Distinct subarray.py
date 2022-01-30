'''
2. Distinct subarray

Number of odd sub arrays. Find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer, two subarrays are 
considered different if they either start or end at different index.

Input:
1
3
1 2 3

Output:4

Explanation: subarrays [[1, [1, 2) [1, 2, 3], [2], [2, 3], [3]]'''

#**************************************************SOLUTION*****************************************************#

def OddSum(a,n):
    r=0
    # Find sum of all subarrays and increment result if sum is odd
    for i in range(n):
        s=0
        for j in range(i,n):
            s=s+a[j]
            if (s%2 != 0):
                r +=1
    return r

t=int(input())
a=[]
while(t!=0):
    n=int(input())
    for i in range(n):
        a.append(int(input()))
    print(OddSum(a,n))
    t-=1
    
