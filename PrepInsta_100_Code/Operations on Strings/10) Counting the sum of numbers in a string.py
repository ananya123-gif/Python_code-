# Counting the sum of numbers in a string

# Input:  string=“4PREP2INSTAA6”
# Output: 12

def count_sum_num(s):
    c=0
    for i in s:
        if(i.isdigit()):
            c+=int(i)
    return c

s=input()
print(count_sum_num(s))
