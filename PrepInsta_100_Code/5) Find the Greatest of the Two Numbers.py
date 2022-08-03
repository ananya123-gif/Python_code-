# Find the Greatest of the Two Numbers
# Given two integer inputs as number1 and number2, the objective is to find the largest among the two.
# Therefore we’ll write a code to Find the Greatest of the Two Numbers in Python Language.

# Example
# Input : 20 40
# Output : 40

def greatest_two_number(num1,num2):
    sol=max(num1,num2)
    return sol
  
num1,num2=map(int,input().split(" "))
print(greatest_two_number(num1,num2))
