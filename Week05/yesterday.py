import jdatetime as jdt

today = jdt.date.today()
today_day = today.day
today_month = today.month
today_year = today.year

print(today_year, today_month, today_day)

yesterday = jdt.date(today_year, today_month, today_day - 1).strftime('Yesterday was: %Y, %m, %d')

print(yesterday)
