from datetime import datetime,timedelta
#from datetime import timedelta
dt1=datetime.today()
print(dt1)
dt4=dt1+timedelta(5)
print(dt4)
#now lets get days between of these two dates
print(dt4-dt1)