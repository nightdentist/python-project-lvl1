#!/usr/bin/env python3
from random import randint
import prompt


GREETING = "Welcome to the Brain Games!"
EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_QUESTION_QTY = 3
CORRECT = 'Correct!'

def welcome_user():
    print (GREETING)
    name = prompt.string("May I have your name?\n")
    print (f"Hello, {name}!")
    print (EXERCISE)
    return name


def get_next_question_and_correct_answer():
    question = randint(1 , 20)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


def play_game(name):
    good_answers = 0
    while good_answers < MAX_QUESTION_QTY:
        question, correct_answer = get_next_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = input ("Your answer: ")
        if user_answer == correct_answer:
            good_answers +=1
            print(CORRECT)
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    play_game(name)


if __name__ == '__main__':
    main()