from datetime import date
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))  # 365 days, 5:01:00

now = datetime.now()
print("Today is", now)

afteroneyear = now + timedelta(days=365)
print("Next year is", afteroneyear.strftime("%A %B %d, %Y"))


