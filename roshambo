import random

# ASCII art for the choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Mapping choices to art
choices = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# Game logic
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "draw"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors (Roshambo)!")
    print("Best of 3 rounds — first to 2 wins is the champion!\n")

    user_score = 0
    computer_score = 0
    rounds = 1

    while user_score < 2 and computer_score < 2 and rounds <= 3:
        print(f"🕹️ Round {rounds}")
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if user_choice not in choices:
            print("⚠️ Invalid choice, please try again.\n")
            continue

        comp_choice = random.choice(list(choices.keys()))

        # Display both choices
        print(f"\nYou chose {user_choice}:")
        print(choices[user_choice])
        print(f"Computer chose {comp_choice}:")
        print(choices[comp_choice])

        # Determine round winner
        result = determine_winner(user_choice, comp_choice)

        if result == "draw":
            print("🤝 It’s a draw this round!\n")
        elif result == "user":
            print("✅ You win this round!\n")
            user_score += 1
        else:
            print("💻 Computer wins this round!\n")
            computer_score += 1

        rounds += 1

    # Final results
    print("🏁 Final Results:")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("🎉 Congratulations! You are the Roshambo Champion!")
    elif computer_score > user_score:
        print("😈 The computer wins this time!")
    else:
        print("🤝 It’s an overall draw!")

# Run the game
if __name__ == "__main__":
    play_game()
