import prompt

from brain_games.constants import MAX_NUMBER_ROUNDS


def run_game(name, generate_expression_and_answer):
    current_round = 1

    while current_round <= MAX_NUMBER_ROUNDS:
        [expression, correct_answer] = generate_expression_and_answer()

        print(f'Question: {expression}')

        response_user = prompt.string('Your answer: ')
        
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
