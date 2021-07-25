from brain_games.cli import welcome_user


def game_is_even_number():
    gamers_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # написать функцию random_number
    print('Question: ' + 'random_number')
    # написать функцию users_answer
    print('Your answer: ' + 'users_answer')
    
    print("'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, " + gamers_name + '!')