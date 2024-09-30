import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words).upper()

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    
           |   
           |   
           |   
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |   
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |   
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |   
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |   
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |   
        --------
        """,
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
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()  # Letters guessed by the user
    tries = 0
    max_tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print('_ ' * len(word))

    while tries < max_tries and word_letters:
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            guessed_letters.add(guess)
            tries += 1
            print(f"Sorry, {guess} is not in the word.")
        
        print(display_hangman(tries))
        
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(' '.join(display_word))
        print(f"Tries left: {max_tries - tries}\n")
    
    if not word_letters:
        print("Congratulations! You guessed the word correctly!")
    else:
        print(f"Sorry, you've been hanged. The word was {word}.")

if __name__ == "__main__":
    play_hangman()
