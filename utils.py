import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')

def load_user_data() -> dict:
    """Loads the mock user data from the users.json file."""
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {USERS_FILE} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {USERS_FILE}.")
        return {}
