from datetime import datetime
from word_selection import get_random_word
from display import display_hangman, display_leaderboard, GREEN, RESET, RED
from high_score import save_high_score, load_high_scores

def play_hangman():
    """
    This function contains the main logic of the Hangman game.
    It manages the game flow, user input, and game state.
    """
    high_scores = load_high_scores()  # Load the high scores
    display_leaderboard(high_scores)  # Show the leaderboard before starting the game
    player_name = input("Enter your name: ")  # Prompt the player to enter their name
    word = get_random_word()  # Get a random word for the game
    word_letters = set(word)  # Create a set of unique letters in the word
    guessed_letters = set()  # Create an empty set to store letters guessed by the user
    tries = 0  # Initialize the number of incorrect guesses
    max_tries = 6  # Set the maximum number of allowed incorrect guesses
    start_time = datetime.now()  # Record the start time of the game

    print("Welcome to Hangman!")  # Welcome message to the player
    print(display_hangman(tries))  # Display the initial hangman state (no drawings)
    print('_ ' * len(word))  # Display blanks representing each letter in the word

    # Continue the game until the player runs out of tries or guesses all letters
    while tries < max_tries and word_letters:
        guess = input("Guess a letter: ").upper()  # Prompt the user to guess a letter and convert it to uppercase

        # Ensure the player inputs only a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            # If the letter has already been guessed, inform the user
            print("You already guessed that letter.")
        elif guess in word_letters:
            # If the guessed letter is in the word
            guessed_letters.add(guess)  # Add the letter to guessed_letters
            word_letters.remove(guess)  # Remove the letter from word_letters as it's been guessed
            print(f"{GREEN}Good job! {guess} is in the word.{RESET}")  # Inform the user of the correct guess
        else:
            # If the guessed letter is not in the word
            guessed_letters.add(guess)  # Add the letter to guessed_letters
            tries += 1  # Increment the number of incorrect guesses
            print(f"{RED}Sorry, {guess} is not in the word.{RESET}")  # Inform the user of the incorrect guess

        print(display_hangman(tries))  # Display the current state of the hangman after the guess

        # Create a list that shows the current state of the word with guessed letters and blanks
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(' '.join(display_word))  # Display the current state of the word
        print(f"Tries left: {max_tries - tries}\n")  # Show the number of remaining tries

    end_time = datetime.now()  # Record the end time of the game
    game_duration = str(end_time - start_time)  # Calculate the game duration

    # Calculate the score using the basic score calculation method
    score = 100 / len(word)

    # After the loop, determine if the player has won or lost
    if not word_letters:
        # If there are no more letters to guess, the player has won
        print("Congratulations! You guessed the word correctly!")
    else:
        # If the player has used all tries, they lose and reveal the word
        print(f"Sorry, you've been hanged. The word was {word}.")

    # Save the high score data
    save_high_score(player_name, score, word, tries, game_duration, list(guessed_letters))

    # Ask the player if they want to play again
    play_again = input(f"{GREEN}Do you want to play again? (yes/no): {RESET}").strip().lower()
    if play_again == 'yes':
        play_hangman()  # Restart the game if the player wants to play again
    else:
        print("Thank you for playing Hangman! Goodbye!")  # Exit message

# This checks if the script is being run directly (not imported) and starts the game
if __name__ == "__main__":
    play_hangman()
