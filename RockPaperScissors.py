import random

user_score = 0
computer_score = 0

while True:
    print("\nRock-Paper-Scissors Game")
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user_choice == "quit":
        print("Final Scores:")
        print(f"You: {user_score}, Computer: {computer_score}")
        print("Thanks for playing!")
        break
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        continue
    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
