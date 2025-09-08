import prompt

from brain_games.games.calculator import calculator
from brain_games.games.check_even import check_even


def start_game():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    number_game = prompt.integer(
        'Choose a game: 1 - "checking for parity", 2 - "calculator" '
    )

    games = {1: check_even, 2: calculator}
    game_func = games.get(number_game)

    if number_game == 1:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif number_game == 2:
        print("What is the result of the expression?")
    elif number_game not in games:
        print("There is no such number\nLet's try again, {user_name}!")

    correct_answers_count = 0

    while correct_answers_count < 3:
        random_number, correct_answer = game_func()
        print(f"Question: {random_number}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again, {user_name}!")
            break

    if correct_answers_count == 3:
        print(f"Congratulations, {user_name}!")
