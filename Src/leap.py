"""Determine whether or not a given data is a leap year"""
 def is_leap_year(year):
    """
    Given a year, return true if the year is a leap year, otherwise return false.
    """
    result = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
        else:
            result = True
    return result
 NON_LEAP_YEARS = [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]
LEAP_YEARS = [1600, 1992, 2000, 2400]
 print("The following are not leap years:")
for y in NON_LEAP_YEARS:
    print("  Is {0} a leap year? {1}".format(y, is_leap_year(y)))
 print("\nThe following are leap years:")
for y in LEAP_YEARS:
    print("  Is {0} a leap year? {1}".format(y, is_leap_year(y)))