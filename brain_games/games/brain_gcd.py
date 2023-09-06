#!/usr/bin/env python3
from math import gcd
from random import randint

from brain_games.games.play_game import play_game

RULES = 'Find the greatest common divisor of given numbers.'


def get_next_question_and_correct_answer():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    correct_answer = gcd(random_number1, random_number2)
    question = str(random_number1) + ' ' + str(random_number2)
    return question, correct_answer


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
