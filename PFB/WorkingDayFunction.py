def GiveWorkingDay():
    from datetime import date
    from datetime import timedelta

    day = date.today()

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)

    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)

    else:
        workingday = day

    print("Working day for",day, "is", workingday)
    return

GiveWorkingDay()

#homework https://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/11772954#overview

def daysTillEndOfYear():

    from datetime import date

    date_today = date.today()
    current_year = date_today.year
    date_endOfYear = date(2022, 12,31)

    delta = date_endOfYear - date_today

    print("till the end of the year it's still:",delta.days,'days')
    return

daysTillEndOfYear()