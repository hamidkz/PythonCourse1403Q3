import datetime as dt

today = dt.date(2024, 11, 14)
today_as_string = today.strftime('%Y/%m/%d ***** %A')

print("Today is : ", today)
print("Today is : ", today_as_string)
