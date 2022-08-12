# Number of days in a given month of a given year
# month = 12
# year = 2012

def leap(year):
    if(year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

def num_of_days(month,year):
    l=[31,28,31,30,31,30,31,30,30,31,30,31]
    if(leap(year)):
        l[1]=29
    return l[month-1]

month=int(input("Enter Month : "))
year=int(input("Enter Year : "))
print(num_of_days(month,year))
