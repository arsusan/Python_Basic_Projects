import random

# Generate a random number between 1 and 20
number_to_guess = random.randint(1, 20)
max_attempts = 5
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 20.")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        
        if guess < 1 or guess > 20:
            print("Your guess is out of range! Please guess a number between 1 and 20.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if attempts == max_attempts and guess != number_to_guess:
    print(f"Game over! The secret number was {number_to_guess}. Better luck next time!")
