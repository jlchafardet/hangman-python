import random

# Load the word list once at the beginning of the script
WORDS = [
    'python', 'hangman', 'challenge', 'programming', 'developer',
    # ... (other words)
]

def get_random_word():
    """
    This function selects and returns a random word from the predefined list of words.
    It uses the random.choice method to pick a word from the WORDS list.
    """
    return random.choice(WORDS).upper()
