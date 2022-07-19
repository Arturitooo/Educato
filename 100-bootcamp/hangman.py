#hangman - day7 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['artur','jest','najlepszym','developerem','pythona','jaki','chodzil','po','tej','planecie']
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")
print(display)

missed_letters = []
lives = 6

while '_' in display:

    guess = input('Guess a letter: ')
    guess = guess.lower()

    if guess in display or guess in missed_letters:
        print('You already typed this letter!')

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = guess
            print('Great, you got this!')
        i += 1
    if guess not in chosen_word:
        missed_letters.append(guess)
        print('\nIm sorry but you missed')
        lives -= 1

    print("--------------------------------------")
    print('\nYour progress:',display)
    print('These letters are not part of the word: ',missed_letters)
    print('Number of lives:', lives)
    print(stages[lives])
    if lives == 0:
        break
if lives == 0:
    print('You lost the game!')
else:
    print('You won, congratulations')
    input()
