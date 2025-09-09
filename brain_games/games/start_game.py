import prompt


def start_game(game_func):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print(game_func.get_description())
    
    correct_answers_count = 0

    while correct_answers_count < 3:
        question, correct_answer = game_func.generate_question()
        print(f"Question: {question}")
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

