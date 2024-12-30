import random

# Constants for the game choices and winning combinations
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

CHOICES = [ROCK, PAPER, SCISSORS]

WINNING_COMBINATIONS = {
    ROCK: SCISSORS,  # Rock beats Scissors
    PAPER: ROCK,     # Paper beats Rock
    SCISSORS: PAPER  # Scissors beats Paper
}

# Function to determine the winner
def rock_paper_scissors(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    
    # Check if the player wins
    if WINNING_COMBINATIONS.get(player_choice) == computer_choice:
        return "Player wins!"
    
    # If not a tie and player didn't win, then computer wins
    return "Computer wins!"

# Main game loop
def play_game():
    while True:
        user_input = input(f"Choose {', '.join(CHOICES)}: ").lower()

        # Ensure valid input
        while user_input not in CHOICES:
            print("Invalid input! Please choose either Rock, Paper, or Scissors.")
            user_input = input(f"Choose {', '.join(CHOICES)}: ").lower()

        computer_input = random.choice(CHOICES)
        result = rock_paper_scissors(user_input, computer_input)

        print(f"Computer chose: {computer_input}")
        print(result)

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()
