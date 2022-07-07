#bootcamp-day2
#data types

#string - names, cities, countries, words etc
#integer - whole numbers, withour decimal places
#float - not whole numbers, with decimals
#boolean - True or False

#Today's application will advise in terms of tips. It can help you if you go to the restaurant with your firneds

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = (float(input("What percentage bill you would like to give? 10, 12 or 15? "))/100)
total_price = (1+tip)*bill
people = int(input("How many people to split the bill? "))
price_per_person = round(float(total_price/people),2)
print(f"Each person should pay: ${price_per_person}")