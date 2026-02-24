from brain_games.constants import MIN_RANDOM_NUMBER
from brain_games.helpers import generate_random_number, is_even

MAX_RANDOM_NUMBER = 100


def generate_expression_and_answer():
    expression = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = 'yes' if is_even(expression) else 'no'

    return [
        expression,
        correct_answer
    ]
