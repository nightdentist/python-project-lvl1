from brain_games.cli import welcome_user
import random
import prompt

def game_is_even_number():
    gamers_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number = str(random.randint(1,30))
    print('Question: ' + number)
    
    answer = prompt.string('Your answer: ')
    
    if int(number) % 2 == 0 and answer == 'yes':
        print('Correct!')
    elif int(number) % 2 == 1 and answer == 'no':
        print('Correct!')
    elif int(number) % 2 == 0:
        print("'" + answer + "'" + " is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + gamers_name + '!')
    elif int(number) % 2 == 1:
        print("'" + answer + "'" + " is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + gamers_name + '!')