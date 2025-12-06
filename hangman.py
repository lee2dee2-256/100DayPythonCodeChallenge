import random
import os

# 🎯 Word bank — used for single-player mode
WORDS = [
    "python", "developer", "hangman", "challenge", "terminal",
    "algorithm", "variable", "function", "object", "inheritance",
    "recursion", "exception", "iteration", "dictionary", "loop"
]

# 🎨 ASCII art for hangman stages
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def clear_screen():
    """Clear terminal screen for cleaner display."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_word():
    """Return a random word from the word bank."""
    return random.choice(WORDS).lower()


def get_player_word():
    """Get a custom word from Player 1 for Player 2 to guess."""
    clear_screen()
    word = input("🧑‍🤝‍🧑 Player 1, enter a word for Player 2 to guess: ").lower().strip()
    while not word.isalpha():
        word = input("⚠️ Please enter only alphabetic characters: ").lower().strip()
    clear_screen()
    print("🔒 Word has been set. Player 2, get ready!\n")
    return word


def display_game_state(word, guessed_letters, attempts_left):
    """Display the hangman, word progress, and guesses."""
    print(HANGMAN_STAGES[len(HANGMAN_STAGES) - attempts_left - 1])
    print("\nWord:", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Attempts left: {attempts_left}\n")


def play_hangman():
    """Main function for Hangman game."""
    clear_screen()
    print("🎮 Welcome to Hangman!")
    print("1️⃣  Single-player (guess a random word)")
    print("2️⃣  Two-player (one sets the word, one guesses)\n")

    mode = input("Choose a mode (1 or 2): ").strip()

    if mode == "1":
        word = get_random_word()
    elif mode == "2":
        word = get_player_word()
    else:
        print("⚠️ Invalid choice. Defaulting to single-player mode.\n")
        word = get_random_word()

    guessed_letters = set()
    attempts_left = len(HANGMAN_STAGES) - 1

    while attempts_left > 0:
        display_game_state(word, guessed_letters, attempts_left)
        guess = input("Enter a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!\n")
        else:
            print("❌ That letter is not in the word.\n")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 You guessed the word: {word.upper()} — You win!")
            break
    else:
        display_game_state(word, guessed_letters, attempts_left)
        print(f"💀 Game Over! The word was: {word.upper()}")


if __name__ == "__main__":
    play_hangman()
