import random

# Initialize scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("===================================")
print("     ROCK PAPER SCISSORS GAME")
print("===================================")
print("Instructions:")
print("- Type rock, paper, or scissors")
print("- Type 'exit' to quit the game")
print("===================================\n")

while True:

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "exit":
        print("\nThanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nCurrent Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Scores:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print("Thanks for playing!")
        break

    print("\n-----------------------------------\n")
