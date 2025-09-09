import prompt

from brain_games.games.calculator import calculator
from brain_games.games.check_even import check_even
from brain_games.games.manual_games import game_instruction
from brain_games.games.brain_gcd import find_gcd
from brain_games.games.brain_progression import encrypt_sequence


def start_game():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    number_game = prompt.integer(
        'Choose a game: 1 - "checking for parity", 2 - "calculator", 3 - "greatest common divisor", 4 - "number missing progression" '
    )

    games = {1: check_even, 2: calculator, 3: find_gcd, 4: encrypt_sequence} # словарь игр для выбора
    game_func = games.get(number_game)

    print(game_instruction(number_game))

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
            print(f"Let's try again, {user_name}!")
            break

    if correct_answers_count == 3:
        print(f"Congratulations, {user_name}!")

