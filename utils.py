import json
from datetime import datetime

def validate_input(input_str, valid_chars):
    """
    Validates that the input string contains only characters from the valid_chars set.
    """
    return len(input_str) == 1 and input_str in valid_chars

def load_json_file(file_path):
    """
    Loads data from a JSON file. Returns an empty dictionary if the file does not exist.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_json_file(file_path, data):
    """
    Saves data to a JSON file.
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def calculate_score(word_length):
    """
    Calculates the score based on the length of the word.
    """
    return 100 / word_length
