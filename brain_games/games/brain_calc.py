from random import randint, choice

from brain_games.games.play_game import play_game

RULES = 'What is the result of the expression?'
MIN_QUESTION_INT = 1
MAX_QUESTION_INT = 20


def get_next_question_and_correct_answer():
    random_num1 = randint(MIN_QUESTION_INT, MAX_QUESTION_INT)
    random_num2 = randint(MIN_QUESTION_INT, MAX_QUESTION_INT)
    random_sign = choice(['+', '-', '*'])
    if random_sign == '+':
        correct_answer = random_num1 + random_num2
    elif random_sign == '-':
        correct_answer = random_num1 - random_num2
    elif random_sign == '*':
        correct_answer = random_num1 * random_num2
    question = str(random_num1) + ' ' + random_sign + ' ' + str(random_num2)
    return question, str(correct_answer)


def run_game():
    play_game(get_next_question_and_correct_answer, RULES)
