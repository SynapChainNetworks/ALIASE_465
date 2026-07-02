import json
import os

PROGRESS_FILE = "token_progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f).get("tokens_mined", 0)
    return 0

def save_progress(tokens):
    with open(PROGRESS_FILE, "w") as f:
        json.dump({"tokens_mined": tokens}, f)
