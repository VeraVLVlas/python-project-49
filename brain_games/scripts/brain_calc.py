from brain_games.launcher import launcher

from brain_games.engine import run_game

from brain_games.scripts.games.calc import generate_expression_and_answer


def main():
    launcher(
        run_game,
        generate_expression_and_answer,
        'What is the result of the expression?'
    )
