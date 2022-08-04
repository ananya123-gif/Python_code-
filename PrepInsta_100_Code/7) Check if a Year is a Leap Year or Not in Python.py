# Check if a Year is a Leap Year or Not in Python
# Given an integer input year, the objective of the code is to Check if a Year is a Leap Year or Not
# in Python Language. To do so  we’ll check if the year input satisfies either of the two conditions of leap year.

# Example
# Input : 2020
# Output : It's a Leap Year.

def check_leap_year(year):
    if(year%4==0 and year%100!=0) or year%400==0:
        print(year,"is Leap Year")
    else:
        print(year,"is not Leap Year")

year=int(input())
check_leap_year(year)
