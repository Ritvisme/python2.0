import random
def computer_guess(x):
    low=50
    high=x
    feedback=" "
    while feedback!='c':
        if low!=high:
            guess=random.randint(low, high)
        else: 
            guess==low
        feedback=input(f'Is {guess} too low(l) or too high(h) or its correct(c)')
        if guess=='h':
            high=guess-1
        elif guess=='l':
            low=guess+1
       
    print('YAY YOU HAVE GUESSED THE CORRECT ANSWER ')


computer_guess(100)