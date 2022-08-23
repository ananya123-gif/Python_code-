# Replace each element by its Rank in the given Array

# Input:  arr = [100, 2, 70, 12 , 90]
# Output: 5 1 3 2 4

def replace_by_rank(arr):
	p=arr.copy()
	arr.sort()
	for i in range(len(p)):
		p[i]=arr.index(p[i])+1
	return p

arr = list(map(int,input().split()))
print(*replace_by_rank(arr))
