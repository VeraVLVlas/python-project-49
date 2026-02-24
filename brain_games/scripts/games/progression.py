from brain_games.constants import MIN_RANDOM_NUMBER
from brain_games.helpers import generate_random_number

MAX_PROGRESSION_LENGTH = 10
MIN_PROGRESSION_LENGTH = 5
MAX_RANDOM_NUMBER = 9

hidden_element = '..'


def generate_arithmetic_progression():
    length_progression = generate_random_number(
        MIN_PROGRESSION_LENGTH,
        MAX_PROGRESSION_LENGTH
    )
    start = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    incremen = generate_random_number(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    progression = [start]
    index = 1

    while index <= length_progression:
        start = start + incremen
        progression.append(start)
        index += 1

    return progression


def hides_number_in_progression(progression):
    length = len(progression) - 1
    random_index = generate_random_number(MIN_RANDOM_NUMBER, length)
    new_prg = progression.copy()
    hidden_number = new_prg[random_index]
    new_prg[random_index] = hidden_element

    return [new_prg, hidden_number]


def generate_expression_and_answer():
    progression = generate_arithmetic_progression()

    [prgs, answer] = hides_number_in_progression(progression)
    
    expression = ' '.join(str(elem) for elem in prgs)
    correct_answer = str(answer)

    return [
        expression,
        correct_answer
    ]
