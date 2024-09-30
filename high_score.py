import json
from datetime import datetime

def save_high_score(player_name, score, word, attempts, game_duration, guesses):
    """
    This function saves the high score data to a JSON file.
    It first creates a dictionary with all the necessary information about the high score.
    Then, it tries to open the existing JSON file to load the current high scores.
    If the file does not exist, it creates a new list to store the high scores.
    Finally, it appends the new high score to the list, sorts the list by score in descending order,
    and writes the updated list back to the JSON file.
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
        # Try to open the existing JSON file to load the current high scores
        with open("hangman_scores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, create a new list to store the high scores
        data = {"high_scores": []}

    # Append the new high score to the list
    data["high_scores"].append(high_score_data)
    # Sort the list by score in descending order
    data["high_scores"].sort(key=lambda x: x["score"], reverse=True)

    # Write the updated list back to the JSON file
    with open("hangman_scores.json", "w") as file:
        json.dump(data, file, indent=4)

def load_high_scores():
    """
    This function loads the high scores from the JSON file.
    If the file does not exist, it returns an empty list.
    """
    try:
        with open("hangman_scores.json", "r") as file:
            data = json.load(file)
            return data["high_scores"]
    except FileNotFoundError:
        return []