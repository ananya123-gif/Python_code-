# Frequency of Elements in an Array

#Input:
# arr = [10, 30, 10, 20, 10, 20, 30, 10]

#Output:
# 10: 4
# 30: 2
# 20: 2

def freq_of_ele(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

arr=[10,30,10,20,10,20,30,10]
print(freq_of_ele(arr))
