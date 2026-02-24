from brain_games.constants import MIN_RANDOM_NUMBER
from brain_games.helpers import generate_random_number

MAX_RANDOM_NUMBER = 100


def find_greatest_common_divisor(num_1, num_2):
    while num_2 != 0:
        temporary = num_1
        num_1 = num_2
        num_2 = temporary % num_2

    return str(num_1)


def generate_expression_and_answer():
    number_1 = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)

    expression = f'{number_1} {number_2}'
    correct_answer = find_greatest_common_divisor(number_1, number_2)

    return [
        expression,
        correct_answer
    ]
