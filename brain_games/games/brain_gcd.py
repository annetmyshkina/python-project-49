

from math import gcd
from random import randint

def find_gcd():
    a = randint(0, 100)
    b = randint(0, 100)

    random_numbers = f'{a} {b}'
    correct_answer = str(gcd(a, b))

    return (random_numbers, correct_answer)

