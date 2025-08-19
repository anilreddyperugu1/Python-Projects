
def check_leap_year(number):
    if number % 4 == 0:
        if number % 100 == 0:
            if number % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def check_days(month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if check_leap_year(year) and month==2:
        return 29
    elif month > 12:
        print("Please enter from 1 to 12")
    else:
        return days_list[month-1]



year = int(input("Enter a year: "))
check_leap_year(year)
month = int(input("Enter a month number(1-12): "))
days=check_days(month)
print(f"The days are {days} days.")
