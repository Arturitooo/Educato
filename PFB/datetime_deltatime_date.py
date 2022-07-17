import datetime

print(datetime.MAXYEAR, datetime.MINYEAR)

d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2, minutes=3)
print(d1+d2)

print(datetime.date.today())

daysToPay = datetime.timedelta(days=7)
print('you have to pay until:', datetime.date.today()+daysToPay)

#how long someone life is

bornDate = datetime.date(2000,8,15)
today = datetime.date.today()

print(today-bornDate)

print(datetime.datetime.today().weekday()+1)