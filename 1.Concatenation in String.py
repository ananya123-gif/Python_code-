
'''1. Concatenation
Input: a string of comma separated numbers. The numbers 5 and 8 are present in the list Assume that 8 always comes after 5.
Case 1: num1 = add all numbers which do not lie between 5 and 8 in the input.
Case 2: num2= numbers formed by concatenating all numbers from 5 to 8.
Output: sum of num1 and num2


Example: 
input: 3,2,6,5,1,4,8,9
Num1 : 3+2+6+9 =20
Num2: 5148
output: 5148+20 = 5168'''


#***************************************SOLUTION**********************************************#

#A comma seprated string 

s=input().split(',')

#Fetch the index of numbers 5 and 8
i_5=s.index('5')
i_8=s.index('8')

#initialize num1 as 0 to store the sum of all values which are not between 5 and 8 
num1=0
for i in range(len(s)):
    if (i<i_5 or i>i_8):
        num1=num1+int(s[i])
        
#initialize num2 as string to join the numbers which comes between 5 and 8   
num2=""
for i in range(i_5,i_8+1):
    num2+=(''.join(s[i]))

#out contain the sum of num1 and num 2 as output 
out=num1+int(num2)
print(out)
