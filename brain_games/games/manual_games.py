
def game_instruction(number_game):
    if number_game == 1:
        return 'Answer "yes" if the number is even, otherwise answer "no".'
    elif number_game == 2:
        return "What is the result of the expression?"
    elif number_game == 3:
        return 'Find the greatest common divisor of given numbers.'
    elif number_game == 4:
        return 'What number is missing in the progression?'
    else:
        return "There is no such number. Let's try again!"