# Given a string, we need to find the minimum number of rotations required to get the same string.
# Examples:
# Input: s = "geeks"
# Output: 5
# Input: s = "aaaa"
# Output: 1

def min_rotation(s):
    s1 = ""
    count = 0
    for i in range(1, len(s) + 1):
        s1 = s[i:] + s[:i]
        count += 1
        if (s1 == s):
            return count

s="geeks"
res=min_rotation(s)
print(res)
