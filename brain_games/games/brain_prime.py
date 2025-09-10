
from random import randint


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    random_number = randint(0, 100)
    divider = 0  
     
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            divider += i
            break
    correct_answer = 'yes' if divider == 0 else 'no'
    return (random_number, correct_answer)



