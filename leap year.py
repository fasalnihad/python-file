#functions to check if the year is leap year 

def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0)or (year % 400 == 0):
        return True
    else:
        return False
    

# ask users to entered a year

year = int(input("enter a year"))

# checking and printing if the year is leap year or not

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")



