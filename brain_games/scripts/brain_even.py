import random

import prompt

from brain_games.cli import welcome_user

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
MAX_NUMBER_ROUNDS = 3


def generate_random_number():
    return random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


def is_even(number):
    return number % 2 == 0


def start_game(name):
    current_round = 1

    while current_round <= MAX_NUMBER_ROUNDS:
        number = generate_random_number()
        print(f'Question: {number}')

        response_user = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(number) else 'no'
        
        if correct_answer == response_user:
            print('Correct!')
            if current_round == MAX_NUMBER_ROUNDS:
                print(f'Congratulations, {name}!')
            current_round += 1
        else:
            print(
                f"'{response_user}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(name)
