# Juggling Algorithm for Array Rotation.

# Algorithm
# Step 1 - In this method, divide the array into M sets, where M = GCD(n, k), and then rotate the elements in each set.
# Step 2 - From the number of elements(n) of the array and number of rotations(k) to be made to the array, the GCD(n, k) number of blocks are made.
# Step 3 - Then in each block, shifting will take place to the corresponding elements in the block.
# Step 4 - After all the elements in all the blocks are shifted, the array will be rotated for the given number of times.
# Step 5 - For Example: If we want to rotate the below array by 2 positions.

# 10 20 30 40 50 60

# M = GCD(6, 2) = 2;
# Initial Array:    10 20 30 40 50 60
# First Set Moves:  50 20 10 40 30 60
# Second Set Moves: 50 60 10 20 30 40

import math
def leftRotate(arr, d, n):
     for i in range(math.gcd(d, n)):
         temp = arr[i]
         j = i
         while 1:
             k = j + d
             if k >= n:
                 k = k - n
             if k == i:
                 break
             arr[j] = arr[k]
             j = k
             arr[j] = temp
arr =list(map(int,input("ENTER ARRAY ELEMENTS ").split()))
n = len(arr)
no_of_rotations = 2

print("Array Elements before rotation : ")
print(*arr)
leftRotate(arr, no_of_rotations, n )
print("\nArray Elements after rotation : ")
print(*arr)
