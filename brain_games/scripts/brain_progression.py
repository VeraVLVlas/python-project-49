from brain_games.engine import run_game
from brain_games.launcher import launcher
from brain_games.scripts.games.progression import generate_expression_and_answer


def main():
    launcher(
        run_game,
        generate_expression_and_answer,
        'What number is missing in the progression?'
    )
