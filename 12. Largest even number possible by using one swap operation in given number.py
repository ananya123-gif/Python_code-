# Given an odd number in the form of a string, the task is to make the largest even number from the given number, and you are allowed to do only one swap operation.
# Examples : 

# Input : 1235785
# Output :1535782
# Swap 2 and 5.

# Input :  536425
# Output :  536524
# Swap 4 and 5 to make the largest even number.

def even_number(s):
    n=len(s)
    f = -1
    l_en = -1
    ln = n - 1
    for i in range(n):
        if (int(s[i]) % 2 == 0 and int(s[i]) < int(s[ln])):
            f = i
            break

        if int(s[i]) % 2 == 0:
            l_en = i
    if f != -1:
        (s[f],s[ln]) = (s[ln],s[f])
        return s
    if f == -1 and l_en != -1:
        (s[l_en],s[ln]) = (s[ln],s[l_en])
        return s
    return s

s="1235785"
res="".join(even_number(list(s)))
print(res)
