from datetime import datetime
st="23/04/2023"
dt3=datetime.strptime(st,"%d/%m/%Y").strftime("%d/%m/%Y")
print(dt3)
#dt1=datetime.today()
#print(dt1)
#print(type(dt1))
#print(type(dt3))
#a=dt3>dt1
#print(a)