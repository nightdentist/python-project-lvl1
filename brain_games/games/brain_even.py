#!/usr/bin/env python3
from random import randint

from brain_games.games.play_game import play_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_next_question_and_correct_answer():
    question = randint(1, 20)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
