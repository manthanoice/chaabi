from datetime import datetime, timedelta

def date_n_days_before(date, n):
    
    date_obj = datetime.strptime(date, '%y-%m-%d')

    new_date_obj = date_obj - timedelta(days=n)

    new_date_str = new_date_obj.strftime('%y-%m-%d')

    return new_date_str

date = '16-12-10'
n = 11

print(date_n_days_before(date, n))