startYear = 1900
startDay = 1
def getDaysForMonth(month, year):
    if month == 1:
        centuryLogic = True
        if year%100==0:
            centuryLogic = False
            if year%400==0:
                centuryLogic = True
        if year%4==0 and centuryLogic:
            return 29
        else: 
            return 28
    if month == 3 or month == 5 or month == 8 or month == 10:
        return 30
    else:
        return 31

sundayMonths = 0
lastMonth = 0
for year in range(startYear, 2001):
    for month in range(0,12):
        if year == startYear and month == 0:
            lastMonth = getDaysForMonth(month,year)
            continue
        startDay = (startDay + lastMonth) % 7
        lastMonth = getDaysForMonth(month,year)
        if startDay == 0 and year >= 1901:
            print(year, month)
            sundayMonths = sundayMonths + 1
print(sundayMonths) #171