import csv 
questions = []

with open("practice/questions.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        formatted_question = {
            "question": row["Question"],

            "options": [row["Opt1"], row["Opt2"], row["Opt3"], row["Opt4"]],

            "answer": row["Answer"]

        }

        questions.append(formatted_question)
    print(questions)