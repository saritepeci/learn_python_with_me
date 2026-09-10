from datetime import date
from datetime import datetime


today = date.today()
print(today)


print("Date components:", today.year, today.month, today.day)

print("Weekday:", today.weekday())

# Datetime
now = datetime.now()
print(now)


