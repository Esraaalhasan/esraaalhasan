import csv
import json

def load_quiz_data(filename='qa.txt'):
  quiz_data = []
  with open("qa.txt", encoding='utf-8') as file:
    questions = file.readlines()
    for question in questions:
      parts = question.strip().split(' - ')
      if len(parts) == 2:
        quiz_data.append({'السؤال': parts[0].strip(), 'الإجابة': parts[1].strip()})
  return quiz_data

def run_quiz(quiz_data):
  correct_answers = 0
  for question_data in quiz_data:
    print(question_data['السؤال'])
    user_answer = input('الإجابة: ')
    if user_answer.strip().lower() == question_data['الإجابة'].strip().lower():
      print('صحيح!')
      correct_answers += 1
    else:
      print(f'خطأ! الإجابة الصحيحة هي: {question_data["الإجابة"]}')
  return correct_answers

def save_results(username, correct_answers, format='csv'):
  if format == 'csv':
    with open('quiz_results.csv', 'a', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow([username, correct_answers])
  elif format == 'json':
    with open('quiz_results.json', 'a') as jsonfile:
      json.dump({'اسم المستخدم': username, 'عدد الإجابات الصحيحة': correct_answers}, jsonfile)
      jsonfile.write('\n')

if __name__ == '__main__':
  quiz_data = load_quiz_data()

  username = input('أدخل اسم المستخدم: ')

  correct_answers = run_quiz(quiz_data)

  print(f'عدد الإجابات الصحيحة: {correct_answers}')

  save_results(username, correct_answers, format='csv') 
  save_results(username, correct_answers, format='json') 







