import random  # Import the random module to select random items from a list
import json  # Import the json module to handle JSON data
from datetime import datetime  # Import datetime to record the date and time

# Define ANSI color codes
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
BROWN = "\033[33m"
WHITE = "\033[37m"

def get_random_word():
    """
    This function selects and returns a random word from a predefined list of words.
    """
    words = [
        'python', 'hangman', 'challenge', 'programming', 'developer',
        'algorithm', 'function', 'variable', 'syntax', 'exception',
        'iteration', 'recursion', 'compiler', 'interpreter', 'debugging',
        'inheritance', 'polymorphism', 'encapsulation', 'abstraction',
        'lambda', 'database', 'framework', 'library', 'module',
        'package', 'virtualization', 'encryption', 'compression',
        'deployment', 'container', 'orchestration', 'binary', 'cache',
        'optimization', 'parallelization', 'threading', 'asynchronous',
        'synchronization', 'networking', 'protocol', 'architecture',
        'interface', 'middleware', 'scalability', 'firewall', 'kernel',
        'router', 'switch', 'gateway', 'bandwidth', 'latency'
    ]  # Expanded list of possible words
    
    chosen_word = random.choice(words)  # Randomly select a word from the list
    return chosen_word.upper()  # Return the chosen word in uppercase letters

def display_hangman(tries):
    """
    This function returns the current state of the hangman based on the number of incorrect guesses (tries).
    """
    stages = [
        # Stage 0: No parts of the hangman are drawn
        f"""
           {BROWN}------
           |    |
           |    
           |   
           |   
           |   
        --------{RESET}
        """,
        # Stage 1: Head is drawn
        f"""
           {BROWN}------
           |    |
           |    {WHITE}O{RESET}
           |   
           |   
           |   
        --------{RESET}
        """,
        # Stage 2: Head and torso are drawn
        f"""
           {BROWN}------
           |    |
           |    {WHITE}O{RESET}
           |    {WHITE}|{RESET}
           |   
           |   
        --------{RESET}
        """,
        # Stage 3: Head, torso, and one arm are drawn
        f"""
           {BROWN}------
           |    |
           |    {WHITE}O{RESET}
           |   {WHITE}/|{RESET}
           |   
           |   
        --------{RESET}
        """,
        # Stage 4: Head, torso, and both arms are drawn
        f"""
           {BROWN}------
           |    |
           |    {WHITE}O{RESET}
           |   {WHITE}/|\\{RESET}
           |   
           |   
        --------{RESET}
        """,
        # Stage 5: Head, torso, both arms, and one leg are drawn
        f"""
           {BROWN}------
           |    |
           |    {WHITE}O{RESET}
           |   {WHITE}/|\\{RESET}
           |   {WHITE}/ {RESET}
           |   
        --------{RESET}
        """,
        # Stage 6: Full hangman is drawn (final stage)
        f"""
           {BROWN}------
           |    |
           |    {WHITE}O{RESET}
           |   {WHITE}/|\\{RESET}
           |   {WHITE}/ \\{RESET}
           |   
        --------{RESET}
        """
    ]
    return stages[tries]  # Return the hangman stage corresponding to the number of tries

def save_high_score(player_name, score, word, attempts, game_duration, guesses):
    """
    This function saves the high score data to a JSON file.
    """
    high_score_data = {
        "player_name": player_name,
        "score": score,
        "date_time": datetime.now().isoformat(),
        "word_guessed": word,
        "attempts": attempts,
        "game_duration": game_duration,
        "difficulty_level": "default",
        "guesses": guesses
    }

    try:
        with open("hangman_scores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"high_scores": []}

    data["high_scores"].append(high_score_data)

    with open("hangman_scores.json", "w") as file:
        json.dump(data, file, indent=4)

def play_hangman():
    """
    This function contains the main logic of the Hangman game.
    It manages the game flow, user input, and game state.
    """
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

# This checks if the script is being run directly (not imported) and starts the game
if __name__ == "__main__":
    play_hangman()