#bootcamp_day5_password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_of_letters=int(input("How many letters would you like in your password? "))
nr_of_symbols=int(input("How many symbols would you like? "))
nr_of_numbers=int(input("How many numbers would you like? "))

password =[]    

for nr in range(0,nr_of_letters):
    password.append(random.choice(letters))

for nr in range(0,nr_of_symbols):
    password.append(random.choice(symbols))

for nr in range(0,nr_of_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

password_string = ""

for n in range(0,len(password)):
    password_string += password[n]

print("Here is your password:",password_string)
