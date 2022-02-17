import math
from math import sqrt

from datetime import datetime, timezone
from datetime import date
from dateutil import tz

print(math.sqrt(9))
print(sqrt(25))

today_date = date(year=2021, month=11, day=16)
print(today_date)
 
# print(datetime.today()) # Actual Date
print(datetime.today().strftime('%Y-%m-%d'))
# print(datetime.today())
print(datetime.now().isoformat()) # Actual Date

print(datetime.today().strftime('%Y-%d-%m'))# Including format date
# print(datetime.today().strftime('%Y-%m-%d %H:%M')) # Taking milliseconds out
print(datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))# Including days of the week
# print(datetime.today(tz.tzlocal)) # Actual Date
print(datetime.now(timezone.utc)) # Actual Date
print(datetime.today())
