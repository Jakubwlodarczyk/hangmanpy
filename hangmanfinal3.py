#HANGMAN 1.6
#!/usr/bin/python3
import random
import time
import os
import sys


Capitals = ["TIRANA", "ANDORRA LA VELLA", "YEREVAN", "VIENNA", "BAKU", 
            "MINSK", "BRUSSELS", "SARAJEVO", "SOFIA", "ZAGREB", "NICOSIA", "PRAGUE", 
            "COPENHAGEN", "TALLINN", "HELSINKI", "PARIS", "TBILISI", "BERLIN", "ATHENS", 
            "BUDAPEST", "REYKJAVIK", "DUBLIN", "ROME", "ASTANA", "PRISTINA", "RIGA", 
            "VADUZ", "VILNIUS", "LUXEMBOURG", "SKOPJE", "VALLETTA", "CHISINAU", "MONACO", 
            "PODGORICA", "AMSTERDAM", "OSLO", "WARSAW", "LISBON", "BUCHAREST", "MOSCOW", 
            "SAN MARINO", "BELGRADE", "BRATISLAVA", "LJUBLJANA", "MADRID", "STOCKHOLM", 
            "BERN", "ANKARA", "KYIV", "LONDON", "VATICAN CITY"]

#alphabeth contains a letters you can use is game (with a space key)
ALPHABETH = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']


#this definition check out the user input, if it is in ALPHABETH,
#changing the input for capital letters
#and checking if you allready type this one letter
def guess_letter(letters_guessed):
    while True:
        guess = input('Guess a letter: ').upper()
        if guess not in ALPHABETH:
            print('_____________________________________________________________')  
            print(guess, '\nWrong sign! Try to type a single letter from A-Z')
        elif guess in letters_guessed:
            print('_____________________________________________________________')
            print('\nYou already guessed this letter!')
            print("Your types:",(letters_guessed))
        else:
            return guess

#the same like guess_letter, but you can type a whole word
def guess_word(letters_guessed):
    while True:
        guess = input('Guess a word: ').upper()
        if guess not in ALPHABETH:
            print('_____________________________________________________________')  
            print(guess, '\nWrong sign! Try to type a word from letters A-Z')
        else:
            return guess


#it clears the terminal screen,
#setting life points
#changing the WORDS , to hidden words, and showing the "_" instead
def play_hangman():
    os.system('clear')
    life_points = 5
    word_to_guess = random.choice(Capitals)
    word_to_guess_spaced = ' '.join(word_to_guess)

    hidden = ['_']*len(word_to_guess)

    letters_guessed = set()
    words_guessed = set()
    user_guessed_word_spaced = ' '.join(hidden)

    print("""          ***************                                                
          *               *                                                
          *               *                                                
          *               *                                                
          *               *                                                
          *               xD                                                 
          *               |                                               
          *               /\\                                               
          *               |                                              
          *               /\                                              
          *                                                              
          *                                                                                                                          
          *                                                              
  ***********************""") 
    print('_____________________________________________________________')
    print("Welcome in HANGMAN GAME!")
    print("We have choose one of the capital of European countries")
    print("Try to guess what is it... Good luck!")
    print("\n")
    print("The word is:\n",user_guessed_word_spaced,"\n")
#set up the menu
    print("Available options: ")
    print("1 - Guess letters")
    print("2 - Guess whole word")
    print("3 - Quit")
    
    op = input("Please, make your decision: ")
    print("\n")


    if op == '1':
        while life_points > 0:
            print(user_guessed_word_spaced)
            user_guess = guess_letter(letters_guessed)
            letters_guessed.add(user_guess)

            if user_guess in word_to_guess:
                print('_____________________________________________________________')
                print("Good job! Letter {} is in the word!".format(user_guess))
                print("Life points:",life_points)
                print("Your types:",(letters_guessed))
                print('\n')

                for i, letter in enumerate(word_to_guess):
                    if user_guess == letter:
                        hidden[i] = letter

                user_guessed_word_spaced = ' '.join(hidden)

                if user_guessed_word_spaced == word_to_guess_spaced:
                    print
                    print(word_to_guess)
                    break
            else:
                print('_____________________________________________________________')
                print("{} is not in this word! Try again!".format(user_guess))
                life_points -= 1
                print("Life points:",life_points)
                print("Your types:",(letters_guessed))
                print('\n')

        return user_guessed_word_spaced == word_to_guess_spaced
    
    elif op == '2':
        while life_points > 0:
            print(user_guessed_word_spaced)
            user_guess = guess_word(words_guessed)
            words_guessed.add(user_guess)

            if user_guess == word_to_guess:
                print(word_to_guess)
                print('\nYou win! GREAT JOB!')
                time.sleep(5)
                play_hangman()
                break
            else:
                print('_____________________________________________________________')
                print("{} is not this word! Try again!".format(user_guess))
                life_points -= 1
                print("Life points:",life_points)
                print("Your types:",(words_guessed))
                print('\n')

        return user_guessed_word_spaced == word_to_guess_spaced
    
    elif op == '3':
        print("Bye!")
        quit()
    else:
        print("Please, try again!")
        time.sleep(2.5)
        play_hangman()

if __name__ == '__main__':

    is_winner = play_hangman()
    if is_winner:
        print('\nYou win! GREAT JOB!')
        time.sleep(5)
        play_hangman()
    else:
        print('\nGAME OVER')
        print('Try again!')
        time.sleep(3.5)
        play_hangman()
