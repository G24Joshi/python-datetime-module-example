from datetime import datetime
dt=datetime.now()
print(dt)
x=dt.strftime("%d-%m-%Y-%H:%M:%S")
file=f"filename_{x}.txt"
print(file)