# Length of the String using Recursion
def length_of_string(s):
    if s == "":
        return 0
    return 1 + length_of_string(s[1:])

s=input()
print(length_of_string(s))
