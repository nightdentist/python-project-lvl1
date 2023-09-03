#!/usr/bin/env python3

MAX_QUESTION_QTY = 3


def play_game(name):
    good_answers = 0
    while good_answers < MAX_QUESTION_QTY:
        question, correct_answer = get_next_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            good_answers += 1
            print('Correct!')
        else:
            usr_answ = (f"'{user_answer}' is wrong answer ;(. ")
            cor_answ = (f"Correct answer was '{correct_answer}'.")
            print(usr_answ + cor_answ)
            print(f"Let's try again, {name}!")
            return