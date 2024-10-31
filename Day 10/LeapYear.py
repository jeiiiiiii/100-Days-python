def is_leap_year(year):

    if year % 4 == 0:
        return "True"
    if year % 100 == 0:
        return "False"
    elif year % 400 == 0:
        return "True"
    else:
        return "False"
    
year = int(input("Enter the year: "))
print(is_leap_year(year))