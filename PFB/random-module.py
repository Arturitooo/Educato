#random - testing / basics

import random

print("Here's one random number:",random.randint(1,100)) #we're drawing one random number in range 1-100

print("Choosing one random number from a range:",random.choice(range(1,100))) #we're choosing random number // here range might be list of names too

print("Choosing one random number from a range - easier:", random.randrange(1,100))


list = ['Art', 'Niuta', 'Tom', 'Kapsi']
print(list)
random.shuffle(list)
print("Reordered list:", list)

print('Just a random float:',random.random())

# homework - https://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/11728158#overview
print("homework - task1")
for i in range(1,10):
    print(random.randint(1,100))

print("homework - task2")
number1 = random.randint(1,100)
print('number 1 is:', number1)
i=1
x=0

while x != number1:
    x = random.randint(1,100)
    i += 1
    print('drawn number;',x)

print('number 1 = 2  is:', number1)
print('to find the same number we had to try ',i,' times')

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)

groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print('Group:',groupNumber)
    print(countries[i])