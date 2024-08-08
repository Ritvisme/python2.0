import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton'}
--snip--
# Loop through all 50 states, making a question for each.
for questionNum in range(50):
# Get right and wrong answers.
 correctAnswer = capitals[states[questionNum]]
 wrongAnswers = list(capitals.values())
 del wrongAnswers[wrongAnswers.index(correctAnswer)]
 wrongAnswers = random.sample(wrongAnswers, 3)
 answerOptions = wrongAnswers + [correctAnswer]
 random.shuffle(answerOptions)
 for i in range(4):
  quizFile.write(f" {'ABCD'[i]}. { answerOptions[i]}\n")
quizFile.write('\n')
# Write the answer key to a file.
answerKeyFile.write(f"{questionNum + 1}.
{'ABCD'[answerOptions.index(correctAnswer)]}")
quizFile.close()
answerKeyFile.close()
