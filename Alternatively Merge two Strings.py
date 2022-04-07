# Given 2 strings, merge them in an alternate way, 
# i.e. the final string’s first character is the first character of the first string,
# the second character of the final string is the first character of the second string and so on. 
# And if once you reach end of one string while if another string is still remaining then append the remaining of that string to final string. 

# Examples: 

# Input : string 1 :"geeks"
#         string 2 :"forgeeks"
# Output: "gfeoerkgseeks"
  
# Explanation : The answer contains characters from alternate strings, and once 
# the first string ends the remaining of the second string is added to the final string

# Input : string 1 :"hello"
#         string 2 :"geeks"
# Output : "hgeelelkos"


def alt_merge(string1,string2):
    res = ""
    i=0
    for i in range(len(string1)):
        res+=string1[i]
        res+=string2[i]
        i+=1

    if(len(string1)>len(string2)):
        res+=string1[i:]
    else:
        res+=string2[i:]
    return res

string1="hello"
string2="geeks"
print(alt_merge(string1,string2))
