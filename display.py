from datetime import datetime

# Define ANSI color codes
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
BROWN = "\033[33m"
WHITE = "\033[37m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
LIGHT_GRAY = "\033[37m"

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
    return stages[tries]

def display_leaderboard(high_scores):
    """
    This function displays the top 5 high scores with color coding.
    """
    print("Leaderboard:")
    for i, score in enumerate(high_scores[:5]):
        color = GREEN if i == 0 else (YELLOW if i == 1 else (BLUE if i == 2 else WHITE))
        print(f"{color}{i + 1}. {score['player_name']} - {score['score']} - {score['date_time']} - {score['word_guessed']}{RESET}")
