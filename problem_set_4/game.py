import random

def main():
    # Runs guessing game
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError
            break
        except ValueError:
            continue

    # Generate secret number
    secret_number = random.randint(1, level)

    # Start guessing loop
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        # Get guess
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()

