import random
def  play():
    user=input("'r' for rock , 's' for scissor, 'p'  for paper ")
    computer=random.choice(['r' , 's' , 'p'])
    if user==computer:
     
        print(f" IT IS A TIE, the computer chose {computer} and you also chose {computer}")
    if is_win(user,computer):
       print(f"YOU WON AS YOU CHOSE {user} but the computer chose {computer}")
    
    
def is_win(player,opponent):
    if(player=='r' and opponent=='s') or (player=="p" and opponent=="r")or (player=="s" and opponent=="p"):
     return True
    
       
print(play())