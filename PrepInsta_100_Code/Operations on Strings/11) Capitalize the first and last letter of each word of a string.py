# Capitalize the first and last letter of each word of a string

# Input:  Enter the String :Prepinsta
# Output: PrepinstA

def capitalize_first_last(s):
    return s[0:1].upper()+s[1:len(s)-1]+s[-1].upper()

s="Prepinsta"
print(capitalize_first_last(s))
