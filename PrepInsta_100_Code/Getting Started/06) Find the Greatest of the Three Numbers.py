# Find the Greatest of the Three Numbers
# Given three integer inputs the objective is to find the largest among them.

# Example
# Input : 20 30 10
# Output : 30

def greatest_three_number(num1,num2,num3):
    sol=max(num1,num2,num3)
    return sol
  
num1,num2,num3=map(int,input().split(" "))
print(greatest_three_number(num1,num2,num3))
