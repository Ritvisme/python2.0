#a=float(input("ENTER THE FIRST NUMBER"))
#b=float(input("ENTER THE FIRST NUMBER"))
#c=float(input("ENTER THE FIRST NUMBER"))
#d=float(input("ENTER THE FIRST NUMBER"))
#e=float(input("ENTER THE FIRST NUMBER"))
#f=float(input("ENTER THE DIVISOR NUMBER"))
#if a%f==0:
    #print('multiple of ',f,"is",a)
#elif b%f==0:
    #print('multiple of ',f,"is",b)
#elif(c%f==0):
    #print('multiple of ',f,"is",c)
#elif(d%f==0):
    #print('multiple of ',f,"is",d)
#lif( e%f==0):
    #print('multiple of ',f,"is",e)
#else:
  #  print("no multple found")

# FACTORIAL OF A NUMBER USING RECURSION

#def factorial(n):
 #return 1 if (n==1 or n==0 ) else  n*factorial(n-1)
#sum=7
#print('the factorial of the number is ',factorial(sum))

# SIMPLE INTEREST
#a=int(input("ENTER THE PRINCIPAL AMOUNT"))
#b=int(input("ENTER THE RATE OF INTEREST"))
#c=int(input("ENTER THE DURATION"))
#simple_interest=a*b*c//100
#print(simple_interest)

#compund interest

#def compound_interest(principal,rate,time):
 # Amount=principal*(pow((1+rate/100),time))
 # CI=Amount-principal
 # print(" THE COMPOUND INTEREST AS PER YOUR DETAILS IS ",CI)
#compound_interest(10000,10.25,5)

#ARMSTRONG NUMBER

##n=int(input("ENTER THE NUMBER"))
##s=n
##b=len(str(n))
##sum1=0
##while n!=0:
  ##r=n%10
  ##sum1=sum1+(r**b)
  ##n=n//10
##if s==sum1:
  #print("THE NUMBER YOU ENTERED WAS",s,"IS A ARMSTRONG NUMBER")
#else:
  #print("THE NUMBER YOU ENTERED IS NOT A ARMSTRONG NUMBER")

  #to check if the string is a pallindrome or not

#def isPalindrome(s):
 #   return s == s[::-1]


# Driver code
#s = "NAMAN"
#ans = isPalindrome(s)

#if ans:
 #   print("Yes")
#else:
  #  print("No")

#use of Decorators

#def make_pretty(func):

    #def inner():
    #  #  print("I got decorated")
      #  func()
    #return inner()



#@make_pretty
#def ordinary():
    #print("I am ordinary")

#ordinary()
#import random
#def computer_guess(x):
#    low=1
#    high=x
#    feedback=" "
#    while feedback!='c':
#        if low!=high:
#            guess=random.randint(low, high)
#        else:
#            guess=low
#            feedback=input(f'Is {guess} too low(l) or too high(h) or its correct(c)')
#        if guess=='h':
#            high=guess-1
#        elif guess=='l':
#            low=guess+1
#
#    print('YAY YOU HAVE GUESSED THE CORRECT ANSWER ')
#
#computer_guess(100)

#hangman game 
#import random
#from words import words
#import string
#def get_valid_words(words):
#    word=random.choice(words)
#    # since the words also contain dashes and spaces we need to account for that 
#    while "-" or " " in words:
#        word=random.choice(words)
#        return word.upper
#def hangman():
#    word=get_valid_words(words)
#    word_letters=set(word)
#    alphabet=set(string.ascii_uppercase)
#    used_letters=set()
#    lives=10
#    while len(word_letters)>0 and lives>0:
#        print("YOU HAVE LIVES LEFT",lives)
#        print("YOU HAVE USED LETTERS".join(used_letters))
#        word_list=[letter if letter in used_letters else '-'  for letter in word]
#        print("current word"," ".join(word_list))
#        input_letter=input("GUESS A LETTER").upper()
#        if input_letter in alphabet-used_letters:
#           # print("you have already used this letter , try a different one ")
#            used_letters.add(input_letter)
#            if (input_letter in word_letters ):
#                word_letters.remove(input_letter)
#            else:
#                lives -= 1
#
#        elif input_letter in used_letters:
#            print("the letter thaat you have used is not part of the words database ")
#    if (lives==0):
#        print ("you have run out of lives lol and the word was {word}")
#    else:
#        print("you have guessed the word correcctly and it is {word}")
#
#hangman()
#          

import random
from words import words
import string 
#def get_valid_words(words):
#    word=random.choice(words)
#    #since the words also have dashes and spaces
#    while "-" or " " in words:
#        word=random.choice(words)
#        return word.upper()
#def hangman():
#        word=get_valid_words(words)
#        #letters in the word
#        word_letters=set(word)
#        alphabet=set(string.ascii_uppercase)
#        #what the user has guessed
#        used_letters=set()
#        LIVES=10
#        #getting the user input
#        while len(word_letters)>0 and LIVES>0:
#
#          print("YOU HAVE LIVES LEFT",LIVES)
#          print("YOU HAVE USED THESE LETTERS"," ".join(used_letters))
#          #what current word is and if it is not in the random word then a dash is shown
#          word_list=[letter if letter in used_letters else "-" for letter in word]
#          print("current word"," ".join(word_list))
#          user_letter=input("GUESS A LETTER:").upper()
#          if user_letter in alphabet-used_letters:
#            used_letters.add(user_letter)
#            if user_letter in word_letters:
#              word_letters.remove(user_letter)
#            else:
#              LIVES-=1
#              print("the letter that you guessed is not a part of this word ")
#          elif user_letter in used_letters:
#            print("you have already guessed this letter, please try again")
#   #gets here when the word_letters==0
#        if (LIVES==0):
#            print(f"WHOOPS, YOU HAVE RUN OUT OF LIVES BUT THE WORD WAS {word}")
#        else:
#            print(f"you have guessed the word correctly and it was {word} ")
#hangman()




def histogram (s):
    d=dict(Í
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
t=['spam','bacon','eggs']
histogram(t)
