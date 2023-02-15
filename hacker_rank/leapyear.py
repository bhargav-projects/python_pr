def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
print(is_leap(1999))


def is_leap(year):
    leap = False
    if year %4==0:
        if year %100==0:
##if year is centure year we need to check with 400
            if year %400==0:
                return True
            else :
                return leap
        else:
            return  True
    else :
        return leap
year =1992
print(is_leap(year))