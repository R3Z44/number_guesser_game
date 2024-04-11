import random

def generate_random_number(start: int, end: int) -> int:
    """
    Generate a random number between start and end
    """
    return random.randint(start, end)


if __name__ == "__main__":
    print (generate_random_number(1,100))
    