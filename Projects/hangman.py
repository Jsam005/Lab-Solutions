import random
import time

print('***** WELCOME TO HANGMAN *****')
time.sleep(2)

print('\nHere are the rules:')
time.sleep(2)

print('*A word will be chosen at random. You have a maximum of 6 incorrect guesses before your character is hanged from the gallows.')
time.sleep(5)

print('\nTRY TO SAVE HIM...GOOD LUCK!')


hang_board = ['''
    |-----|
          |
          |
          |
          |
    ========''', '''
    |-----|
    O     |
          |
          |
          |
    ========''', '''
    |-----|
    O     |
    |     |
          |
          |
    ========''', '''
    |-----|
    O     |
   \|     |
          |
          |
   ========''', '''
    |-----|
    O     |
   \|/    |
          |
          |
   ========''', '''
    |-----|
    O     |
   \|/    |
   /      |
          |
   ========''', '''
    |-----|
    O     |
   \|/    |
   / \    |
          |
   ========''']

words = 'cat dog run hit sit sea moon sun here cool pool bee see fox box eyes hello there apple salad glass dress robot' \
        'tiger shark suits paris money clown plane snake piano sunshine friendly revolution italian egyptian japanese ' \
        'florists scientist astronauts astronomy creature tequila galaxies irrelevant australia madagascar'.upper().split()

random.shuffle(words)

correct_letters = []
incorrect_letters = []
secret_word = words.pop()

def rand_word():
    pass

def display_board():
    # shows the gallows, displays the secret word as '_' and will print the letters guessed incorrectly
    blanks = '_' * len(secret_word)

    for i in secret_word:
        if i in correct_letters:
            print(i, end=' ')
        elif i not in correct_letters or i not in secret_word:
            print(blanks, end=' ')

        if i in incorrect_letters:
            print(i, end=' ')

    print("\n\nIncorrect letters guessed so far: {} ".format(incorrect_letters))
    print(hang_board[len(incorrect_letters)])

def guesses():
    # allows the user to guess, then appends the letter to the correct or incorrect list

    while True:

        guess = input("\nEnter a letter: ").upper()

        if guess in correct_letters or guess in incorrect_letters:
            print("\nYOU HAVE ALREADY GUESSED THAT LETTER.")
        elif guess.isnumeric():
            print("\nINVALID ENTRY. PLEASE ENTER LETTERS ONLY.")
        elif len(guess) > 1:
            print("\nPLEASE ENTER ONLY ONE LETTER AT A TIME.")
        else:
            break

    if guess in secret_word:
        correct_letters.append(guess)
    else:
        incorrect_letters.append(guess)

def check_win():
    # check to see if the user has won or lost the game

    if len(incorrect_letters) >= 6:
        return 'loser'

    for letter in secret_word:
        if letter not in correct_letters:
            return 'no win'
    return 'winner'

def main():

    # rand_word()

    while True:

        display_board()
        guesses()
        is_winner = check_win()

        if is_winner is 'loser':
            print("***** GAME OVER!!! YOU'VE HANGED HIM, SHAME ON YOU! ***** The secret word was {} ".format(secret_word))
            print(hang_board[6])
            break

        if is_winner is 'winner':
            print("***** GOOD JOB!!! YOU SAVED HIM FROM THE GALLOWS! ***** The secret word was {} ".format(secret_word))
            break

main()