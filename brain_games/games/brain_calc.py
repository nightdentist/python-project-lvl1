#!/usr/bin/env python3
from random import randint
from random import choice

import prompt

from brain_games.cli import welcome_user


MAX_QUESTION_QTY = 3
CORRECT = 'Correct!'


def print_exerrsise():
    print('What is the result of the expression?')


def get_next_question_and_correct_answer():
    random_number1 = randint(1, 20)
    random_number2 = randint(1, 20)
    random_arithmetic_sign = choice(['+', '-', '*'])
    if random_arithmetic_sign == '+':
        correct_answer = random_number1 + random_number2
    elif random_arithmetic_sign == '-':
        correct_answer = random_number1 - random_number2
    else:
        correct_answer = random_number1 * random_number2
    question = str(random_number1) + ' ' + random_arithmetic_sign + ' ' + str(random_number2)
    return question, correct_answer


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
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def run_game():
    name = welcome_user()
    print_exerrsise()
    play_game(name)
    