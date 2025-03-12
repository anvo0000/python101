import datetime

now = datetime.datetime.now()
print(f"now: {now}")
year = now.year
month = now.month
day = now.day
print(year, month, day)

date_of_birth = datetime.datetime(year=1999,
                                  month=9,
                                  day=29)
print(f"date_of_birth: {date_of_birth}")



current_date_of_week = now.weekday()
print(f"current_date_of_week: {current_date_of_week}")