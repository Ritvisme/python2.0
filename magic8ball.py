import  random
def getAnswer(answerNumber):
 if answerNumber == 1:
  return 'my name is Pratham '
 elif answerNumber == 2:
    return 'i love cars'
 elif answerNumber == 3:
    return 'i am passionate about skating'
 elif answerNumber == 4:
    return 'what is your name?'
 elif answerNumber == 5:
    return 'i love playing football'
 elif answerNumber == 6:
    return 'we have exams from 16th november'
 elif answerNumber == 7:
    return 'halo'
 elif answerNumber == 8:
    return 'Lucifer is the best series ever!'
 elif answerNumber == 9:
    return "Web series choices is subjective"
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
