from pathlib import Path
import json

ioput = "Chapter 10/favorite_number.json"


def load_favorite_number(path):
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"Your favorite number is {favorite_number}.")


def save_favorite_number(path):
    path = Path(path)
    favorite_number = input("What's your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f"Wrote {favorite_number} to {path}.")


def get_favorite_number():
    path = Path(ioput)
    if path.exists():
        load_favorite_number(path)
    else:
        save_favorite_number(path)


get_favorite_number()