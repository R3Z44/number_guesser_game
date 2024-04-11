def get_valid_input(start, end):
    """
    Get a valid input from the user
    """
    while True:
        try:
            user_guess = int(input(f"Enter a number between {start} and {end}: "))
            if start <= user_guess <= end:
                return user_guess
            else:
                print(f"Invalid input. Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

if __name__ == "__main__":
    print(get_valid_input(1, 100))