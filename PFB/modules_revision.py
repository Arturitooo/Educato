#homework https://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/8291362#overview

import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print(len(inputdata))
print(len(factortable))

if len(inputdata) == len(factortable):
    for n in range(len(inputdata)):
        minivalue = inputdata[n]-factortable[n]*inputdata[n]
        minInteger = math.floor(minivalue)
        maxvalue = inputdata[n]+factortable[n]*inputdata[n]
        maxInteger = math.ceil(maxvalue)
        print(minInteger,inputdata[n],maxInteger)
    print("ok")
else:
    print("inputdata and factortable need to have equal number of elements")

#task nr2
import random

for n in range(len(inputdata)):
    minivalue = inputdata[n]-random.random()*inputdata[n]
    minInteger = math.floor(minivalue)
    maxvalue = inputdata[n]+random.random()*inputdata[n]
    maxInteger = math.ceil(maxvalue)
    print(minInteger,inputdata[n],maxInteger)

#task nr3

import datetime

print(datetime.datetime.today())
#print(datetime.datetime.today(year,month,day))