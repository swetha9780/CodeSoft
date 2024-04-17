import random

def play_game():
    # Define the choices available in the game
    choices = ['rock', 'paper', 'scissors']
    
    # Prompt the user to choose rock, paper, or scissors
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Validate user input
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Generate computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
    else:
        result = "You lose!"
    
    # Display choices and result
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)
    
    return result

def main():
    # Initialize scores for user and computer
    user_score = 0
    computer_score = 0
    
    # Main game loop
    while True:
        # Play a round
        result = play_game()
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display scores
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
