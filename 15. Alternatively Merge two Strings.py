# Given 2 strings, merge them in an alternate way, 
# i.e. the final string’s first character is the first character of the first string, 
# the second character of the final string is the first character of the second string and so on. 
# And if once you reach end of one string while if another string is still remaining then append the remaining of that string to final string 

# Examples: 
# Input : string 1 :"geeks"
#         string 2 :"forgeeks"
# Output: "gfeoerkgseeks"

# Explanation : The answer contains characters from alternate strings, and once 
# the first string ends the remaining of the second string is added to the final string

# Input :string 1 :"hello"
#        string 2 :"geeks"
# Output : hgeelelkos

def merge(s1,s2):
    res=""
    i=0
    while(i<len(s1) or i<len(s2)):
        if(i<len(s1)):
            res+=s1[i]
        if(i<len(s2)):
            res+=s2[i]
        i+=1
    return res

s1="geeks"
s2="forgeeks"
print(merge(s1,s2))
