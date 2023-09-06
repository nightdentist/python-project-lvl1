#!/usr/bin/env python3
from random import randint, choice

from brain_games.games.play_game import play_game

RULES = 'What is the result of the expression?'


def get_next_question_and_correct_answer():
    random_num1 = randint(1, 20)
    random_num2 = randint(1, 20)
    random_sign = choice(['+', '-', '*'])
    if random_sign == '+':
        correct_answer = random_num1 + random_num2
    elif random_sign == '-':
        correct_answer = random_num1 - random_num2
    else:
        correct_answer = random_num1 * random_num2
    question = str(random_num1) + ' ' + random_sign + ' ' + str(random_num2)
    return question, correct_answer


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
