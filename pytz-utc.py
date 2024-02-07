import pytz
from datetime import datetime
d1=datetime.now()
d2=datetime.now(pytz.UTC)
print(d1)
print(d2)
