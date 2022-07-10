import time
 
# sprawdzenie wersji pythona
import sys
#print(sys.version)
 
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
#print(time.perf_counter(), time.localtime(time.perf_counter()))

import time

#the time below is unix time counted in seconds since 1 January 1970
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.localtime(time.perf_counter())))

import calendar
print(calendar.month(2017,9,w=5,l=1))
print(calendar.month(2017,9))

print('Week day is:',calendar.weekday(2017,9,29)+1)
calendar.setfirstweekday(6) #we're setting here Sunday as first week day - only in drawing aspect (it counts monday still when it comes to variables)
print(calendar.month(2017,9))

print("We've had",calendar.leapdays(2000,2007),'leap days in years 2000-2006')

#these modules are used to print calendar rather, then to calculations - in timedelta, date and datetime modules we will focus on calculations

#homework https://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/11740920#overview
print('\nhomework\n')

print(time.time())
print(time.asctime(time.localtime(time.time())))

print(calendar.month(1995,10))
calendar.setfirstweekday(4)
print(calendar.month(1995,10))

if calendar.leapdays(2000,2001)>0:
    print('2000 was leap year')
else:
    print("2000 wasn't leap year")

print(calendar.month(2019,12))