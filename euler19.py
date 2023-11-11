# Project Euler 19 - https://projecteuler.net/problem=19 - Lösung 171

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days_per_month = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

days_per_month_leap = {
    1 : 31,
    2 : 29,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}


def sundaycount():
    start = 1901
    end = 2000
    sum_sundays_on_first = 0
    kalendertag = 2

    for year in range(start, end+1):
        for month in range(1, 12+1):

            if year % 4 == 0:
                for days in range(1,days_per_month_leap[month]+1):
                    if kalendertag == 7:
                        if days == 1:
                            sum_sundays_on_first += 1
                        kalendertag = 0
                    kalendertag += 1
    

            else:
                for days in range(1,days_per_month[month]+1):
                    if kalendertag == 7:
                        if days == 1:
                            sum_sundays_on_first += 1
                        kalendertag = 0
                    kalendertag += 1 
        

    return sum_sundays_on_first

print(sundaycount())