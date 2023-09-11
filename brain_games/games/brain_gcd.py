from random import randint

from brain_games.games.play_game import play_game

RULES = 'Find the greatest common divisor of given numbers.'
MIN_QUESTION_INT = 1
MAX_QUESTION_INT = 100


def get_next_question_and_correct_answer():
    random_number1 = randint(MIN_QUESTION_INT, MAX_QUESTION_INT)
    random_number2 = randint(MIN_QUESTION_INT, MAX_QUESTION_INT)
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
