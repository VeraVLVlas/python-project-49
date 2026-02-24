from brain_games.engine import run_game
from brain_games.launcher import launcher
from brain_games.scripts.games.prime import generate_expression_and_answer


def main():
    launcher(
        run_game,
        generate_expression_and_answer,
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
