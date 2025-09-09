from random import randint


def get_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    random_number = randint(0, 100)
    correct_answer = "yes" if random_number % 2 == 0 else "no"

    return (random_number, correct_answer)
