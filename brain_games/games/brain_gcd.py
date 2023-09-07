#!/usr/bin/env python3
from random import randint

from brain_games.games.play_game import play_game

RULES = 'Find the greatest common divisor of given numbers.'


def get_next_question_and_correct_answer():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = str(random_number1) + ' ' + str(random_number2)
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 = random_number1 % random_number2
        else:
            random_number2 = random_number2 % random_number1
    correct_answer = random_number1 + random_number2
    return question, correct_answer


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
