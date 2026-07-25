import random
import string

def hangman():
    words = ["python", "apple", "stream", "planet", "guitar"]
    secret = random.choice(words)
    guessed = set()
    wrong = set()
    max_wrong = 6

    def display_word():
        return " ".join([ch if ch in guessed else "_" for ch in secret])

    print("Welcome to Hangman!")
    print(f"You have {max_wrong} incorrect guesses. Good luck!\n")

    while len(wrong) < max_wrong and not all(ch in guessed for ch in secret):
        print("Word: ", display_word())
        print(f"Wrong guesses ({len(wrong)}/{max_wrong}): {', '.join(sorted(wrong)) if wrong else '-'}")
        guess = input("Guess a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single letter (a-z).\n")
            continue
        if guess in guessed or guess in wrong:
            print("You already tried that letter.\n")
            continue

        # Apply guess
        if guess in secret:
            guessed.add(guess)
            print("Nice! That letter is in the word.\n")
        else:
            wrong.add(guess)
            print("Nope! That letter is not in the word.\n")

    # Outcome
    if all(ch in guessed for ch in secret):
        print("Congratulations! You guessed the word:", secret)
    else:
        print("Out of guesses! The word was:", secret)

if __name__ == "__main__":
    hangman()
