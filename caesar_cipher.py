import argparse

def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """Encrypt or decrypt a text using the Caesar cipher algorithm."""
    result = ""

    # Invert shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char  # Keep spaces, punctuation, etc.

    return result

def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt text using the Caesar cipher."
    )
    parser.add_argument("text", help="The text to encrypt or decrypt.")
    parser.add_argument("shift", type=int, help="The number of letters to shift.")
    parser.add_argument(
        "-m", "--mode",
        choices=["encrypt", "decrypt"],
        default="encrypt",
        help="Choose operation mode (default: encrypt)."
    )

    args = parser.parse_args()
    output = caesar_cipher(args.text, args.shift, args.mode)

    # Display result
    print("\n--- Caesar Cipher Result ---")
    print(f"Mode   : {args.mode.capitalize()}")
    print(f"Shift  : {args.shift}")
    print(f"Input  : {args.text}")
    print(f"Output : {output}")
    print("-----------------------------\n")

if __name__ == "__main__":
    main()
