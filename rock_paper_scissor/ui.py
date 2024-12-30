import tkinter as tk
import random

# Function to determine the winner
def rock_paper_scissors(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    
    elif player_choice == "rock":
        if computer_choice == "scissors":
            return "Player wins!"
        else:
            return "Computer wins!"
    
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "Player wins!"
        else:
            return "Computer wins!"
    
    elif player_choice == "scissors":
        if computer_choice == "paper":
            return "Player wins!"
        else:
            return "Computer wins!"
    else:
        return "Invalid choice!"

# Function to update the result and computer's choice
def play(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = rock_paper_scissors(player_choice, computer_choice)
    
    # Update the UI with results
    result_label.config(text=result)
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    
    # Disable the play buttons and show the play again button
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")
    play_again_button.pack(pady=10)

# Function to reset the game
def play_again():
    # Reset the game state
    result_label.config(text="")
    computer_choice_label.config(text="")
    
    # Re-enable the play buttons
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")
    
    # Hide the play again button
    play_again_button.pack_forget()

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Add instruction label
instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instruction_label.pack(pady=10)

# Buttons for user to choose Rock, Paper, or Scissors
rock_button = tk.Button(window, text="Rock", font=("Arial", 12), width=10, command=lambda: play("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", font=("Arial", 12), width=10, command=lambda: play("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("scissors"))
scissors_button.pack(pady=5)

# Label to show the computer's choice
computer_choice_label = tk.Label(window, text="", font=("Arial", 12))
computer_choice_label.pack(pady=10)

# Label to show the result
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Play Again button (initially hidden)
play_again_button = tk.Button(window, text="Play Again", font=("Arial", 12), command=play_again)

# Start the Tkinter event loop
window.mainloop()
