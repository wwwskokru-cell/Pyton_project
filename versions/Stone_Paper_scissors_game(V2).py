import random

OPTIONS = ["stone", "paper", "scissors"]
WIN_RULES = {
    ("stone", "scissors"): "Computer wins!",
    ("scissors", "paper"): "Computer wins!",
    ("paper", "stone"): "Computer wins!",
}

def get_winner(user, computer):
    if user == computer:
        return "Draw!"
    return WIN_RULES.get((computer, user), "You win!")

def play_game():
    computer_choice = random.choice(OPTIONS)
    user_choice = input("Choose stone, paper or scissors: ").lower().strip()
    
    while user_choice not in OPTIONS:
        print("Invalid choice! Please choose: stone, paper, scissors")
        user_choice = input("Your choice: ").lower().strip()
    
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"Result: {get_winner(user_choice, computer_choice)}")
