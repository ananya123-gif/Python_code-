# Given a string of size n,
# write functions to perform the following operations on a string-
# Left (Or anticlockwise) rotate the given string by d elements (where d <= n)
# Right (Or clockwise) rotate the given string by d elements (where d <= n).

# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe"
#          Right Rotation : "ksGeeksforGee"

def leftrotate(s,d):
    n=len(s)
    if(d<=n):
        res=s[d:]+s[:d]
        return res

def rightrortate(s,d):
    n=len(s)
    if(d<=n):
        res=s[n-d:]+s[:n-d]
        return res

s = "qwertyu"
d = 2
l=leftrotate(s,d)
r=rightrortate(s,d)
print(l)
print(r)
