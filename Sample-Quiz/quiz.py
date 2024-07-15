def ask_question(question, options, correct_index):
  """
  This function asks a question with multiple choices and checks the user's answer.
  """
  print(question)
  for i, option in enumerate(options):
    print(f"{i+1}. {option}")

  user_answer = int(input("Enter your answer (1, 2, 3, etc.): ")) - 1

  return user_answer == correct_index

def main():
  """
  This function contains the main quiz logic.
  """
  # Define your quiz questions here as a list of dictionaries.
  # Each dictionary should have keys: question, options, and answer_index (index of the correct answer in options)
  questions = [
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin"], "answer_index": 1},
    # Add more questions here following the same format
  ]

  score = 0
  for question in questions:
    if ask_question(question["question"], question["options"], question["answer_index"]):
      score += 1
      print("Correct!")
    else:
      print("Incorrect.")

  print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
  main()