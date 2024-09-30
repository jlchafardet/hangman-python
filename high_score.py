from datetime import datetime
from utils import load_json_file, save_json_file

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

    data = load_json_file("hangman_scores.json")
    if "high_scores" not in data:
        data["high_scores"] = []

    data["high_scores"].append(high_score_data)
    data["high_scores"].sort(key=lambda x: x["score"], reverse=True)

    save_json_file("hangman_scores.json", data)

def load_high_scores():
    """
    This function loads the high scores from the JSON file.
    """
    data = load_json_file("hangman_scores.json")
    return data.get("high_scores", [])