#!/usr/bin/env python3
from random import randint

import prompt

from brain_games.cli import welcome_user


MAX_QUESTION_QTY = 3
CORRECT = 'Correct!'


def print_exerrsise():
    print('What number is missing in the progression?')


def get_next_question_and_correct_answer():
    start_progression_number = randint(1, 5)
    fihish_progression_number = 25
    interval_of_progression = randint(2, 4)
    progression = list(range(start_progression_number, fihish_progression_number, interval_of_progression))
    index = randint(1, 3)
    correct_answer = progression[index]
    progression[index] = '..'
    question_progression = list(progression)
    question = " ".join(map(str, question_progression))
    return question, correct_answer


def play_game(name):
    good_answers = 0
    while good_answers < MAX_QUESTION_QTY:
        question, correct_answer = get_next_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
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
