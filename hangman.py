import random

# 🎯 Word bank — you can expand this list or load from a file
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


def get_random_word():
    """Return a random word from the word bank."""
    return random.choice(WORDS).lower()


def display_game_state(word, guessed_letters, attempts_left):
    """Display the current hangman stage, word progress, and guesses."""
    print(HANGMAN_STAGES[len(HANGMAN_STAGES) - attempts_left - 1])
    print("\nWord:", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Attempts left: {attempts_left}\n")


def play_hangman():
    """Main function to play Hangman."""
    print("🎮 Welcome to Hangman!")
    print("Guess the word before the hangman is fully drawn.\n")

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
            print("✅ Nice! That letter is in the word.\n")
        else:
            print("❌ Oops! That letter is not in the word.\n")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: {word.upper()}")
            break
    else:
        display_game_state(word, guessed_letters, attempts_left)
        print(f"💀 Game Over! The word was: {word.upper()}")


if __name__ == "__main__":
    play_hangman()
