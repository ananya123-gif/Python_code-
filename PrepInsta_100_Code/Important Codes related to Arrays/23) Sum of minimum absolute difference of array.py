# Sum of minimum absolute difference of array
# arr = [2, 5, 4, 3]
# Required Sum = 4

def sum_min_absolute(arr):
	n=len(arr)
	arr.sort()
	s=0
	s+=abs(arr[0]-arr[1])
	s+=abs(arr[n-1]-arr[n-2])
	for i in range(1,n-1):
		s+=min(abs(arr[i]-arr[i-1]),abs(arr[i]-arr[i+1]))
	return s

arr=list(map(int,input().split()))
print(sum_min_absolute(arr))
