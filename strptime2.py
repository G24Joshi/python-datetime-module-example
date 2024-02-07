from datetime import datetime
dob="31/12/1994"
d1=datetime.strptime(dob,"%d/%m/%Y")
print("old date:",d1)
d2=datetime.today()
print("Current date:",d2)
diff=d2-d1
d=diff.days
print("days:",d)