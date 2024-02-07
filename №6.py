def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365

def date_to_days(date):
    day, month, year = date
    days = 0
    for y in range(1, year):
        days += days_in_year(y)
    for m in range(1, month):
        if m == 2 and is_leap_year(year):
            days += 1
