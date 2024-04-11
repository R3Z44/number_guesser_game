def get_valid_input(start, end):
    """
    Get a valid input from the user
    """
    status = True
    while status:
        try:
            user_guess = input(f"Enter a number between {start} and {end}: ")
            if user_guess == "q":
                print("Thank you for playing! Good Bye!")
                status = False
                break
            else:
                user_guess = int(user_guess)
                if start <= user_guess <= end:
                    return user_guess
                else:
                    print(
                        f"Invalid input. Please enter a number between {start} and {end}.")
                    continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


if __name__ == "__main__":
    print(get_valid_input(1, 100))
