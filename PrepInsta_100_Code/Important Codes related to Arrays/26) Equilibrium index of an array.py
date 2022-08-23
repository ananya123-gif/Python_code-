# Equilibrium index of an array
# Input:  a=[4, -2, 0, 6, -4]
# Output: 2

def equilibrium(a):
	for i in range(1,len(a)):
		if(sum(a[:i])==sum(a[i+1:])):
			return i

a=[4,-2,0,6,-4]
print(equilibrium(a))
