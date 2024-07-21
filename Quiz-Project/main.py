from question import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []
for ques in question_data:
    question_text = ques['question']
    question_answer = ques['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = Quiz_Brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    
print("You've completed the quiz!")
print(f'Your final score: {quiz.score}/{quiz.question_number}')
print('\n')