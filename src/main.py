import random




def validate_guess(user_guess):
    
    if not user_guess.isdigit():
        print("Invalid input. Please enter a valid number.")
        return False
    
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1 :
        print ("Invalid input. Please enter a number between 1 and 100.")
        return False
    
    return True


def main():
    score = 100
    random_number = random.randint(1, 100)
    
    while True:
        user_guess = input ("Please enter your guess: ")
        
        if user_guess == "q" :
            print ("Good bye!")
            return False
        
        if not validate_guess(user_guess):
            continue
        
        user_guess = int(user_guess)
        
        print (user_guess)
        if user_guess < random_number:
            print ("Your guess is lower than the target number.")
            score -= 10
            continue
        
        if user_guess > random_number:
            print ("Your guess is higher than the target number.")
            score -= 10
            continue
        
        
        print ("Congrats! You guessed the correct number!")
        print (f"your score is: {score}")
        break


if __name__ == "__main__":
    main()
