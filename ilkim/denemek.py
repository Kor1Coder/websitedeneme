from datetime import datetime
y=datetime.now() .strftime("%m/%d/%Y, %H:%M:%S").split()[0].strip(',').split('/')
u="-".join(y[::-1])
print(u.split('-'))