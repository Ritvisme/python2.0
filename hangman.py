import random
from words import words
import string 
def get_valid_words(words):
    word=random.choice(words)
    #since the words also have dashes and spaces 
    while "-" or " " in words:
        word=random.choice(words)
        return word.upper()
def hangman():
        word=get_valid_words(words)
        #letters in the word
        word_letters=set(word)
        alphabet=set(string.ascii_uppercase)
        #what the user has guessed 
        used_letters=set()
        LIVES=6
        #getting the user input
        while len(word_letters)>0 and LIVES>0:
          
          print("YOU HAVE LIVES LEFT",LIVES)
          print("YOU HAVE USED THESE LETTERS"," ".join(used_letters))
          #what current word is and if it is not in the random word then a dash is shown
          word_list=[letter if letter in used_letters else "-" for letter in word]
          print("current word"," ".join(word_list))
          user_letter=input("GUESS A LETTER:").upper()
          if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
              word_letters.remove(user_letter)
            else:
              LIVES-=1
              print("the letter that you guessed is not a part of this word ")
          elif user_letter in used_letters:
            print("you have already guessed this letter, please try again")
   #gets here when the word_letters==0
        if (LIVES==0):
            print(f"WHOOPS, YOU HAVE RUN OUT OF LIVES BUT THE WORD WAS {word}")
        else:
            print(f"you have guessed the word correctly and it was {word} ")
hangman()