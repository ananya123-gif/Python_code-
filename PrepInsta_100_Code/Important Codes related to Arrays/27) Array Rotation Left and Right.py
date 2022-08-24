# Array Rotation Left and Right

# Example

# Input :arr = [10, 20, 30, 40, 50]
# Output :
# Right rotation by 1 position : 50 10 20 30 40
# Left rotation by 1 position : 20 30 40 50 10

def rotate_left_right(arr,n):
	print("Right Rotation :",arr[(len(arr)-n):]+arr[:(len(arr)-n)])
	print("Left Rotation :",arr[n:]+arr[0:n])

arr=list(map(int,input("Enter elements in array : ").split()))
n=int(input("Enter rotation number : "))
rotate_left_right(arr,n)
