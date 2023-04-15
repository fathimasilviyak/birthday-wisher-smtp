import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond
day_of_week = now.weekday()
print(f"{now}\n{year}\n{month}\n{day}\n{hour}\n{minute}\n{second}\n{microsecond}\n{day_of_week}")

birth_day = dt.datetime(year=1995, month=10, day=5, hour=4)
print(birth_day)
