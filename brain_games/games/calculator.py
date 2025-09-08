from random import choice, randint


def calculator():
    x = randint(0, 100)
    y = randint(0, 100)
    operator = choice(["+", "-", "*"])

    match operator:
        case "+":
            random_expression = f"{x} + {y}"
            correct_answer = str(x + y)
            return (random_expression, correct_answer)
        case "-":
            random_expression = f"{x} - {y}"
            correct_answer = str(x - y)
            return (random_expression, correct_answer)
        case "*":
            random_expression = f"{x} * {y}"
            correct_answer = str(x * y)
            return (random_expression, correct_answer)
