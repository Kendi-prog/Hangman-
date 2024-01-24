import random
from words import words  #importing our variable words from words.py file
import string


#the computer has to randomly select a word for us to guess from the list 
def  guess_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list

    while '-' in word or ' ' in word :
        word = random.choice(words)

    return word.lower()


def hangman():
    word = guess_valid_word(words)
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_lowercase) 
    used_letters = set() #what the user has guessed
    lives = 5
    #getting the user input
    while len(word_letters) > 0 and lives > 0:

     # telling the user the letters used
     #.join() method is used to concatenate or join elements of an iterable, such as a list or tuple, into a single string.
     # ''.join(['a', 'b', 'cd']) --> 'a b cd'
     print('You have ', lives, 'lives left.You have used these characters: ', ' '.join(used_letters))

     # tell the user what the current word is but with dashes eg.(C H - I R)
     word_list = [letter if letter in used_letters else '-' for letter in word] #every single letter the user has guessed is shown and what they havent guessed are just dashes
     print('Current word: ', ' '.join(word_list))

     user_letter = input('Guess a letter: ').lower()
     if user_letter in alphabet - used_letters:  #if the letter guessed is in the alphabet
        used_letters.add(user_letter)   #we then add the letter to the used_letters which is the set which keeps track of what the user has guessed
        if user_letter in word_letters:   #if the letter is in the word we are trying to guess
            word_letters.remove(user_letter)  #we then remove the letter from words_letters set which keeps track of the letters in words.
        else:
           lives = lives - 1  #takes the life away when it is wrong\
           print('Letter not in the word')
     elif user_letter in used_letters:
        print('You have already guessed this character.Try Again.')
     else:
        print('Invalid Character!!!') #this is the output when the user input is not in the alphabet or in the used_letters set

    #stops iterating when the len(word_letters) == 0  OR when lives == 0
    if lives == 0:
        print('You died! The word was ', word)
    else:
        print('Congratulations! You guessed the word ', word,' correctly.')
        
hangman()

