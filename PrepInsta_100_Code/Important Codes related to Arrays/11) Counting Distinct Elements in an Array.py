# Counting Distinct Elements in an Array

# Example

# Input : arr = [10, 20, 40, 30, 50, 20, 10, 20]
# Output : 5
# Explanation : 10, 20, 30, 40, 50 are the distinct elements.

def counting_distinct_ele(arr):
    d=set(arr)
    return len(d)

arr=list(map(int,input().split(" ")))
print(counting_distinct_ele(arr))
