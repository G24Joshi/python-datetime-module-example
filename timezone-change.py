import pytz
from datetime import datetime
d1=datetime.now()
print("Current Time:",d1)
tz=pytz.timezone("Asia/Dubai")
d2=d1.astimezone(tz)
print("Time of Dubai:",d2)
