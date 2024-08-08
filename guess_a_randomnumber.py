import random       #to generate random number
secretnumber=random.randint(1,20) #random number b/w 1 & 20 and storing it in secretnumber variable
print('i am thinking a number between 1 and 20 ')

# letting the player to guess 6 times for the secretnumber you chose
for guessestaken in range(1,7):    #for letting the player guess 6 times
    print('Take a guess')
    guess=int(input())    #taking the users input for the guess
    if guess<secretnumber:
        print('your guess is too low')
    elif guess> secretnumber:
        print('your guess is too high')
    else:
        break       #this is executed when the guess is correct and the loop breaks

if guess==secretnumber:
    print('Good job! You guessed the secret number i thought. for this you have taken  '+str(guessestaken)+' guesses')
else:
    print('Nope. Number i was thinking of was  ' + str(secretnumber))

