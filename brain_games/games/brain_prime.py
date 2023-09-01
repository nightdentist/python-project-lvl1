#!/usr/bin/env python3
from random import randint

import prompt

from brain_games.cli import welcome_user


MAX_QUESTION_QTY = 3
CORRECT = 'Correct!'


def print_exerrsise():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_next_question_and_correct_answer():
    question = randint(1, 50)
    d = 2
    while question % d != 0:
        d += 1
    if d == question:
        correct_answer = 'yes'
        return question, correct_answer
    else:
        correct_answer = "no"
        return question, correct_answer


def play_game(name):
    good_answers = 0
    while good_answers < MAX_QUESTION_QTY:
        question, correct_answer = get_next_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
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
