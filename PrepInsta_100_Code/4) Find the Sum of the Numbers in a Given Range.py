# Find the Sum of the Numbers in a Given Range
# Given two integer inputs as the range [ low , high ],
# the objective is to find the sum of the numbers that lay in the intervals given by the integer inputs.
# Therefore we’ll write a code to Find the Sum of the Numbers in a Given Range in Python Language.

# Example
# Input : 2 5
# Output : 14

def sum_in_range(l,h):
    s=0
    for i in range(l,h+1):
        s+=i
    return s
l,h=map(int,input().split(" "))
print(sum_in_range(l,h))
