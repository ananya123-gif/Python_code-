# Sort Array according to the order defined by Another Array

# Example:
# Input:  arr1 = [ 20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18 ]
# 		  arr2 = [ 20, 1, 18, 39 ]

# Output:	20 20 1 1 18 18 39 5 6 7 9

def sort_ary_order_def_by_another(arr1,arr2):
	l=[]
	l1=[]
	for i in range(len(arr2)):
		for j in range(len(arr1)):
			if(arr2[i]==arr1[j]):
				l.append(arr1[j])
	for i in arr1:
		if i not in l:
			l1.append(i)
	l1.sort()
	return l+l1

arr1 = [ 20, 1, 20, 5, 7, 1, 9, 39, 6, 18, 18 ]
arr2 = [ 20, 1, 18, 39 ]
print(*sort_ary_order_def_by_another(arr1,arr2))
