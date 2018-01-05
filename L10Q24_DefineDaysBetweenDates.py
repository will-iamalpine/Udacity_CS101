# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

#helper function
def dateIsBefore(year1, month1, day1, year2, month2, day2):
        if year2 > year1:
            return True
        if year1 == year2:
            if month2 > month1:
                return True
            if month1 == month2:
                #best solution:
                return day1 < day2
                # my solution with unnecessary logic
            #    if day2 > day1:
            #        return True
            #    if day1 == day2:
            #        return False
            #return False
        return False
#test dateIsBefore
#print dateIsBefore(2012,9,30,2012,9,20)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    if dateIsBefore == False:
        return  "you can't time travel"
    else:
        days_in_months = 30
        months_in_year = 12
        years = 0
        months = 0
        days = 0
        #years
        if year1 <= year2:
            years = year2-year1
        #months
        if month1 <= month2:
            months = month2 - month1
        else:
            months = 12 - month1 + month2
        #days
        if day1 <= day2:
            days = day2 - day1
        else:
            days = 30 - day2 + day1

        return (years*months_in_year*days_in_months) + (months * days_in_months) + days

#print daysBetweenDates(2012,1,1,2013,1,1)

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
