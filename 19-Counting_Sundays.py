def IsLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def IncrementMonth(month, year, count):
    if month == 2:
        if IsLeapYear(year):
            count += 29
        else:
            count += 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        count += 30
    else:
        count += 31

    if month == 12:
        year += 1

    month = (month % 12) + 1

    return (month, year, count)


# count is the number of days since Jan 1, 1900
# since we know that day was a Monday, we can that counter to determine if the
# start of the current month is a Sunday
month, year, count = (1, 1901, 365)
sundays = 0
while year < 2001:
    if count % 7 == 6:
        sundays += 1
    month, year, count = IncrementMonth(month, year, count)

print(sundays)
print(month, year, count)
