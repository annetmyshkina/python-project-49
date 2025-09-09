

from math import gcd
from random import randint


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def generate_question():
    a = randint(0, 100)
    b = randint(0, 100)

    random_numbers = f'{a} {b}'
    correct_answer = str(gcd(a, b))

    return (random_numbers, correct_answer)

