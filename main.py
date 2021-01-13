import random
from art import logo


# METHODS
def choose_number_of_attempts():
    if input("Choose difficulty (type easy or hard): ").lower() == "easy":
        return 10
    else:
        return 5


def will_play_again():
    if input("Play again? (y/n) ").lower() == "y":
        return True
    else:
        return False


# MAIN
print(logo)
print("Welcome to the Number Guessing Game!")

game_is_in_progress = True

while game_is_in_progress:
    attempts_remaining = choose_number_of_attempts()
    number = random.randint(1, 100)
    round_is_in_progress = True

    print("\nI'm thinking of a number between 1 and 100.")

    while round_is_in_progress:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")

        guess = int(input("\nMake a guess: "))

        if guess > number:
            print("Too high")
            attempts_remaining -= 1
        elif guess < number:
            print("Too low")
            attempts_remaining -= 1
        else:
            print(f"You win! The number was {number}")
            round_is_in_progress = False
            game_is_in_progress = will_play_again()
            break

        if attempts_remaining <= 0:
            print(f"\nOut of tries. The number was {number}")
            round_is_in_progress = False
            game_is_in_progress = will_play_again()
            break
