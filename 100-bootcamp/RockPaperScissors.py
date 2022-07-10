#there's quite nice website askpython.com that includes all modules libraries and explanations <- USE IT
#rock paper and scissors
import random
rps = int(input('What do you choose? Type 0 for Rock, 1 por Paper and 2 for Scissors\n'))
possibilities = ["rock","paper","scissors"]

if rps>2 or nps<0:
    print('You put an invalid number, you lose!')

print('You chose:', possibilities[rps])

rand_rps = random.randint(0,2)
print('Computer chose:',possibilities[rand_rps])


if rps == rand_rps:
    print("it's a draw")

if rps == 0 and rand_rps == 1:
    print("You lose")
elif rps == 0 and rand_rps == 2:
    print("You win")
elif rps == 1 and rand_rps == 0:
    print("You win")    
elif rps == 1 and rand_rps == 2:
    print("You lose")
elif rps == 2 and rand_rps == 0:
    print("You lose")    
elif rps == 2 and rand_rps == 1:
    print("You win")
