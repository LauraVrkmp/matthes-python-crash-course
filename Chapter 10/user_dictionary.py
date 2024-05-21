from pathlib import Path
import json

ioput = "Chapter 10/user_dictionary.json"


def load_favorite_number(path):
    contents = path.read_text()
    user_info = json.loads(contents)
    print(f"Your user info is {user_info}.")


def save_favorite_number(path):
    path = Path(path)
    username = input("What's your username? ")
    first_name = input("What's your first name? ")
    last_name = input("What's your last name? ")
    user_info = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"Wrote user info to {path}.")


def get_user_info():
    path = Path(ioput)
    if path.exists():
        load_favorite_number(path)
    else:
        save_favorite_number(path)


get_user_info()