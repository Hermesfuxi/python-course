import datetime

time_now = datetime.datetime.now()
print(time_now)
print(time_now.strftime("%Y-%m-%d %H:%M:%S"))
print(time_now.year)
print(time_now.month)
print(time_now.day)
print(time_now.hour)
print(time_now.minute)
print(time_now.second)

print(datetime.timedelta.max)