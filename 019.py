# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 019 - Counting Sundays
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# ----------------------------------

def f(startYear, finishYear):
    count = 0
    
    # calculate the day of week:
    # (day + month + year + (year/4)+century) mod 7
    dayOfWeek = int((1 + 1 + startYear + (startYear / 4) + 20) % 7)
    
    for year in range(startYear, finishYear+1):
        for month in range(1, 13):
            totalDay = 30 if month in [4, 6, 9, 11] else (29 if year % 4 else 28) if month % 2 == 0 else 30            
            for day in range(1, totalDay+1):
                if dayOfWeek > 6:
                    dayOfWeek = 0
                if dayOfWeek == 0 and day == 1:
                    count += 1
                dayOfWeek += 1               

    return count

anwser = f(1901, 2000)

assert anwser == 171

print 'Answer: ', anwser
