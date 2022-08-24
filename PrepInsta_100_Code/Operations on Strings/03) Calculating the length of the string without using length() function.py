# Calculating the length of the string without using length() function

# Input:  string = 'Hello'
# Output: 5

def cal_len(s):
    c=0
    for i in s:
        c+=1
    return c

s=input("Enter String : ")
print(cal_len(s))
