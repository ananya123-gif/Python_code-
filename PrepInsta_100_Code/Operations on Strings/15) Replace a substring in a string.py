# Replace a substring in a string

# Example:

# Input:
# Enter String : PrepInsta
# Enter substring which has to be replaced : Insta
# Enter substring with which str1 has to be replaced : Ster
# Output:
# String after replacement : PrepSter

def replace_substring(string,sub,rep):
    if sub in string:
        return string.replace(sub,rep)

string = "PrepInsta"
sub="Insta"
rep="Ster"
print(replace_substring(string,sub,rep))
