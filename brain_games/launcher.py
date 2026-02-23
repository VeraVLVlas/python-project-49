from brain_games.cli import welcome_user


def launcher(run_game, generate_expression_and_answer, rules):
    name = welcome_user()
    print(rules)
    run_game(name, generate_expression_and_answer)
