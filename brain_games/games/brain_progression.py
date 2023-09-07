#!/usr/bin/env python3
from random import randint

from brain_games.games.play_game import play_game

RULES = 'What number is missing in the progression?'


def get_next_question_and_correct_answer():
    start_prog = randint(1, 5)
    fihish_prog = 25
    interval_progression = randint(2, 4)
    progression = list(range(start_prog, fihish_prog, interval_progression))
    unknown_number = randint(1, 3)
    correct_answer = progression[unknown_number]
    progression[unknown_number] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
