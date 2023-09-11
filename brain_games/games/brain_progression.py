from random import randint

from brain_games.games.play_game import play_game

RULES = 'What number is missing in the progression?'
MIN_PROGRESSION_INT = 1
MAX_PROGRESSION_INT = 5
INTERVAL_START = 2
INTERVAL_FINISH = 4
UNKNOW_START = 1
UNKNOW_FINISH = 3


def get_next_question_and_correct_answer():
    start_progprogression = randint(MIN_PROGRESSION_INT, MAX_PROGRESSION_INT)
    fihish_progression = 25
    interval_progression = randint(INTERVAL_START, INTERVAL_FINISH)
    progression = list(range(start_progprogression, fihish_progression,
                             interval_progression))
    unknown_number = randint(UNKNOW_START, UNKNOW_FINISH)
    correct_answer = progression[unknown_number]
    progression[unknown_number] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
