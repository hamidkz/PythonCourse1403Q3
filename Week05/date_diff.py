import datetime

today = datetime.date.today()
yesterday = datetime.date(today.year, today.month, today.day - 1)

print(yesterday, today)
one_day = today - yesterday

tomorrow = today + one_day
print(tomorrow)

# day_at_last_week = ?
# for i in range(7):
#     today -= one_day

# print(today)

my_time_delta = datetime.timedelta()
new_date = today + my_time_delta
print(new_date)