import math

from brain_games.constants import MIN_RANDOM_NUMBER
from brain_games.helpers import generate_random_number

MAX_RANDOM_NUMBER = 60


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_expression_and_answer():
    expression = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = 'yes' if is_prime(expression) else 'no'

    return [
        expression,
        correct_answer
    ]
