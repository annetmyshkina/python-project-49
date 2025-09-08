

from random import randint


def check_even():
    
    random_number = randint(0, 100)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'

    return (random_number, correct_answer)
        