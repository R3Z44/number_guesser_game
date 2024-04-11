from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import decrement_score


def main():
    actual_number = generate_random_number(1, 100)
    score = 100
    while True:
        user_guess = get_valid_input(1, 100)
        print(user_guess)
        if user_guess != actual_number:
            score = decrement_score(score)
            provide_hint(user_guess, actual_number)
            continue
        print ("Congratulations!!!! Your guess is correct!!!!")
        print (f"your score is: {score}")
        return True

if __name__ == '__main__':
    main()
