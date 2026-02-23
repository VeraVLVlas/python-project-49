import random

from brain_games.constants import MIN_RANDOM_NUMBER

from brain_games.helpers import generate_random_number

MAX_RANDOM_NUMBER = 20

mathematical_operators = ['+', '-', '*']


def calculate(num_1, num_2, operator):
    if operator == '+':
        answer = num_1 + num_2
    elif operator == '-':
        answer = num_1 - num_2
    elif operator == '*':
        answer = num_1 * num_2
    else:
        answer = 'oops'
    return str(answer)


def generate_numbers_and_operator():
    number_1 = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operator = random.choice(mathematical_operators)
    
    return [number_1, number_2, operator]


def generate_expression_and_answer():
    [number_1, number_2, operator] = generate_numbers_and_operator()
    expression =  f'{number_1} {operator} {number_2}'
    correct_answer = calculate(number_1, number_2, operator)

    return [
        expression,
        correct_answer
    ]
