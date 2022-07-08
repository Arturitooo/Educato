#functions that changes text

line = 'this IS a very STRANGE text'
print(line.capitalize())
print(line.upper())
print(line.title())
print(line.swapcase())
print(line.casefold())

line2 = 'żółć'
print(line2.casefold())
print(line2.replace('ż','z').replace('ó','o'))

print(line.find('e'))
print(line.rfind('e'))
print(line.index('e'))
print(line.find('u'))
# this one gives error print(line.index('u'))

import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)

#transform string into list
list = line.split()
print(list)

#transform list into string
list2 = ' '.join(list)
print(list2)

#homewor - khttps://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/11740460#overview

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp nam legą w prochu i pyle! '''

lines = poem.split('\n')
print(lines)

for i in range(8):
    print(lines[i])
    print(lines[i+8])