# Block Swap Algorithm

# Method:
# Declare two arrays A and B,
# Copy all the elements from index 0 to (d-1) to A[] and from index d to n-1 to B[].
# Run a loop till size of array A is equal to size of B[].
# If A is longer, divide A into Al and Ar such that Al is of same length as B Swap Al and B to change AlArB into BArAl.
# Now B is at its final place, so recur on pieces of A.
# Finally when A and B are of equal size, block swap them.

def block_swap(arr,d):
	n=len(arr)
	if (d == 0 or d == n):
		return
	i = d
	j = n-d
	while (i!=j):
		if (i<j):
			swap(arr,d-i,d+j-i,i)
			j -= i
		else:
			swap(arr,d-i,d,j)
			i -= j
	swap(arr,d-i,d,i)
	return arr

def swap(arr,fi,si,d):
	for i in range(d):
		temp = arr[fi+i]
		arr[fi+i] = arr[si+i]
		arr[si+i] = temp

a=list(map(int,input().split()))
b=int(input())
print(*block_swap(a,b))
