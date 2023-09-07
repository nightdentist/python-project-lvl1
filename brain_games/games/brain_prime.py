#!/usr/bin/env python3
from random import randint

from brain_games.games.play_game import play_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_next_question_and_correct_answer():
    question = randint(2, 50)
    divider = 2
    while question % divider != 0:
        divider += 1
    if divider == question:
        correct_answer = 'yes'
    if divider != question:
        correct_answer = "no"
    return question, correct_answer


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
