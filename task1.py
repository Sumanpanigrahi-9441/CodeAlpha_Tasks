import random

def hangman():
    words = ["python", "code", "alpha", "project", "script"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("=== Hangman Game ===")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord: " + display_word)
        print(f"Remaining attempts: {attempts}")

        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word!")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("❌ Wrong guess!")

    if attempts == 0:
        print(f"\n💥 Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()