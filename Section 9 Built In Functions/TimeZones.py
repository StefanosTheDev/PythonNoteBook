from datetime import datetime, timezone, timedelta
print(datetime.now()) # this is a naive datetime.

today = datetime.now(timezone.utc) # Central Time Universal Time Standard .

tommorrow = today + timedelta(days = 1)
print(today)

print(today.strftime('%d-%m-%Y %H:%M')) #strformat time

user_date = input(' Enter the date in YYYY -mm - Dd format')
user_date = datetime.strptime(user_date, '%Y-%m-%d')
print(user_date)