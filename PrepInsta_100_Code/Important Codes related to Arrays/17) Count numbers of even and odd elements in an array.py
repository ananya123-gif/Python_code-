# Count numbers of even and odd elements in an array

# Example

#Input:   arr = [11, 20, 35, 40, 53]
#Output:  Even Elements count = 2 (20, 40)
#         Odd Elements count = 3 (11, 35, 53)

def num_of_even_odd(arr):
    even=0
    odd=0
    for i in arr:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    print("Even Elements count =",even)
    print("Odd Elements count =",odd)

arr=list(map(int,input().split()))
num_of_even_odd(arr)
