# Check if all the numbers of array can be made equal

# Example

# Input: 	n=3
# 			arr[] =[50, 75, 100]
# Output: 	Yes

# Explanation : [50 * 2 * 3, 75 * 2 * 2, 100 * 3] = [300, 300, 300]

def check_all_made_equal(arr,n):
	for i in range(n):
		while(arr[i]%2==0):
			arr[i]//=2
		while(arr[i]%3==0):
			arr[i]//=3
		if(arr[i]!=arr[0]):
			return False
	return True

n=int(input())
arr=list(map(int,input().split()))
if(check_all_made_equal(arr,n)):
	print("Yes")
else:
	print("No")
