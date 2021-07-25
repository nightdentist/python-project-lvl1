import prompt


def welcome_user():
    print('Welcome to the Brain Games')

    gamers_name = prompt.string('May I have your name? ')

    print('Hello, ' + gamers_name + "!")
    return gamers_name
