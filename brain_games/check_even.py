
import prompt
from random import randint


def check_even():
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0

    while correct_answers_count < 3:
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        user_answer = input("Your answer: ")

        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
            break

    if correct_answers_count == 3:
        print(f'Congratulations, {user_name}!')