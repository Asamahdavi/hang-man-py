import random
import string 
# now i can have access to all words in words file
from words import words
# first step for computer is to guess a word

# this func get the words, then filter them wether they have - or space. 
def valid_wold(words):
    #random.choice job is to choose random item/word from the words
    randWord = random.choice(words)
    while '-' in randWord or ' ' in randWord:
        randWord = random.choice(words)

    return randWord.upper()

def hangman():
    word=valid_wold(words)
    # the letters in the word will be converting to a set call word letters
    word_letters = set(word) 
    # set for all english alphabet for guessing from the user
    alp=set(string.ascii_uppercase)
    # this for tracking what user have been guess 
    used_letters=set()

    # set live for the hang man set limited guesses
    man_lives=6;


    while len(word_letters) >0 and man_lives > 0:
        #show the letters user have been used
        # join(used_letters) this make this set to a string
        print('You have',man_lives,'lives left & you have used these letters: ',''.join(used_letters))
        # show current word 
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ',' '.join(word_list))
        # getting user input , use upper func for handling upper/lower cases
        user_letter= input("Guess a letter: ").upper()
        # first if the user enter a letter which  has been choosen before
        if user_letter in alp - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                man_lives-=1
                print('Input letter is not in the choosen word')
        elif user_letter in used_letters:
            print('you already used that letter. try again')
        else:
            print('invalid letter!!') 
    
    if man_lives == 0 :
        print("Game over !!! The word was", word )
    else:
        print("You won ,",word,"was correct!!!")



hangman()


