import random  # Import the random module to select random items from a list

def get_random_word():
    """
    This function selects and returns a random word from a predefined list of words.
    """
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']  # List of possible words
    chosen_word = random.choice(words)  # Randomly select a word from the list
    return chosen_word.upper()  # Return the chosen word in uppercase letters

def display_hangman(tries):
    """
    This function returns the current state of the hangman based on the number of incorrect guesses (tries).
    """
    stages = [
        # Stage 0: No parts of the hangman are drawn
        """
           ------
           |    |
           |    
           |   
           |   
           |   
        --------
        """,
        # Stage 1: Head is drawn
        """
           ------
           |    |
           |    O
           |   
           |   
           |   
        --------
        """,
        # Stage 2: Head and torso are drawn
        """
           ------
           |    |
           |    O
           |    |
           |   
           |   
        --------
        """,
        # Stage 3: Head, torso, and one arm are drawn
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |   
        --------
        """,
        # Stage 4: Head, torso, and both arms are drawn
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |   
        --------
        """,
        # Stage 5: Head, torso, both arms, and one leg are drawn
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |   
        --------
        """,
        # Stage 6: Full hangman is drawn (final stage)
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |   
        --------
        """
    ]
    return stages[tries]  # Return the hangman stage corresponding to the number of tries

def play_hangman():
    """
    This function contains the main logic of the Hangman game.
    It manages the game flow, user input, and game state.
    """
    word = get_random_word()  # Get a random word for the game
    word_letters = set(word)  # Create a set of unique letters in the word
    guessed_letters = set()  # Create an empty set to store letters guessed by the user
    tries = 0  # Initialize the number of incorrect guesses
    max_tries = 6  # Set the maximum number of allowed incorrect guesses

    print("Welcome to Hangman!")  # Welcome message to the player
    print(display_hangman(tries))  # Display the initial hangman state (no drawings)
    print('_ ' * len(word))  # Display blanks representing each letter in the word

    # Continue the game until the player runs out of tries or guesses all letters
    while tries < max_tries and word_letters:
        guess = input("Guess a letter: ").upper()  # Prompt the user to guess a letter and convert it to uppercase
        
        if guess in guessed_letters:
            # If the letter has already been guessed, inform the user
            print("You already guessed that letter.")
        elif guess in word_letters:
            # If the guessed letter is in the word
            guessed_letters.add(guess)  # Add the letter to guessed_letters
            word_letters.remove(guess)  # Remove the letter from word_letters as it's been guessed
            print(f"Good job! {guess} is in the word.")  # Inform the user of the correct guess
        else:
            # If the guessed letter is not in the word
            guessed_letters.add(guess)  # Add the letter to guessed_letters
            tries += 1  # Increment the number of incorrect guesses
            print(f"Sorry, {guess} is not in the word.")  # Inform the user of the incorrect guess
        
        print(display_hangman(tries))  # Display the current state of the hangman after the guess
        
        # Create a list that shows the current state of the word with guessed letters and blanks
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(' '.join(display_word))  # Display the current state of the word
        print(f"Tries left: {max_tries - tries}\n")  # Show the number of remaining tries
    
    # After the loop, determine if the player has won or lost
    if not word_letters:
        # If there are no more letters to guess, the player has won
        print("Congratulations! You guessed the word correctly!")
    else:
        # If the player has used all tries, they lose and reveal the word
        print(f"Sorry, you've been hanged. The word was {word}.")

# This checks if the script is being run directly (not imported) and starts the game
if __name__ == "__main__":
    play_hangman()