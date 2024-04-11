def provide_hint (user_guess, actual_number):
    if user_guess < actual_number:
        print ("Your guess is lower than the actual number")
        return False
    
    elif user_guess > actual_number:
        print ("Your guess is greater than the actual number")
        return False
