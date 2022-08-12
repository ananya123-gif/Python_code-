# Occurrence of a Digit in a given Number

# Example :
# Input : Enter a number : 897982
#        Enter the digit : 9
# Output :  2

# Explanation : The digit 9 occurs twice

def occurrence_of_digit(num,digit):
    num=str(num)
    digit=str(digit)
    return num.count(digit)

num=int(input("Enter a Number : "))
digit=int(input("Enter the digit : "))
print(occurrence_of_digit(num,digit))
