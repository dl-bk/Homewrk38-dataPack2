# Створіть програму для проведення опитування або
# анкетування. Зберігайте відповіді користувачів у форматі
# JSON файлу. Кожне опитування може бути окремим
# об'єктом у файлі JSON, а відповіді кожного користувача -
# списком значень.

import json


FILENAME = "answers.json"

def save_data(filename, ans):
    try:
        with open(filename, 'r') as rfile:
            data = json.load(rfile)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    data.append(ans)

    with open(filename, 'w') as wfile:
        json.dump(data, wfile, indent =2)
    
    print("data saved")

def start_survey(questions):
    answer = {}
    for question in questions:
        print(question)
        current_ans = input("-> ")
        answer[question] = current_ans
    
    return answer



questions = [
    "What is your name?",
    "How old are you?",
    "Where are you from?",
    "Which languages you speak?",
    "What is your favourite color?"
]

answer = start_survey(questions)
save_data(FILENAME, answer)
print(answer)