import random

def get_computer_choice():
    """Randomly choose Rock, Paper, or Scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # Get user choice
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Check if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
