import json
import os

file_path = os.path.join(os.path.dirname(__file__), '../schedule.json')

def save_schedule(posts):
    with open(file_path, "w") as f:
        json.dump(posts, f)

def load_schedule():
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
