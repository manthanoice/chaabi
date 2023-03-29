from datetime import datetime, timedelta

def dates_within_difference(from_date, to_date, difference):
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')

    delta = abs(to_datetime - from_datetime)

    # print(delta)
    # print(delta.days)

    delta_days = delta.days

    return delta_days < difference

from_date = '21-03-20'
to_date = '22-03-20'
difference = 2

print(dates_within_difference(from_date, to_date, difference)) 