# Calculate The  Frequency of a Characters

# Input:  str = "YOLO LIFE"
# Output: {'Y': 1, 'O': 2, 'L': 2, ' ': 1, 'I': 1, 'F': 1, 'E': 1}

def freq_of_char(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

s=input("Enter String : ")
print(freq_of_char(s))
