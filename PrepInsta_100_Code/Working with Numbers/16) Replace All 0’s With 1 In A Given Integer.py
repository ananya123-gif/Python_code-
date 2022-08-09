# Replace All 0’s With 1 In A Given Integer
# Input:  10250
# Output: 11251

def zero_one(num):
    num=str(num)
    num=num.replace('0','1')
    num=int(num)
    return num

num=int(input())
print(zero_one(num))
