

from random import choice, randint


def get_description():
    return 'What number is missing in the progression?'


def generate_question():
    sequence = get_progression()
    random_element = str(choice(sequence))  
    question_sequence = ['..' if j == random_element else j for j in sequence]
    return ' '.join(question_sequence), random_element


def get_progression():
    length_progression = choice([5, 6, 7, 8, 9, 10, 11, 12])
    start = randint(0, 20)
    step = randint(1, 10)  
    a_progression = [str(start + i * step) for i in range(length_progression)]
    return a_progression
