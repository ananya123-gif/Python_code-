# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings

def longest_common_Prefix(strs):
    if strs:
        first_s = s[0]
    else:
        return ""

    for ele in strs:
        res=""
        for j in range(len(ele)):
            if(len(first_s)<=j):
                break
            elif (ele[j]==first_s[j]):
                res+=ele[j]
            elif (ele==0):
                return ""
            else:
                first_s=res
        first_s=res
    return res

s=["flower","flow","flight"]
print(longest_common_Prefix(s))
