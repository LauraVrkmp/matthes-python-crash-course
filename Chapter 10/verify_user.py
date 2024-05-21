from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = "Chapter 10/user_name.json"
    path = Path(path)
    username = get_stored_username(path)
    if username:
        answer = input(f"Are you {username}? (y/n) ")
        if answer == 'y':
            print(f"Welcome back, {username}!")
            return
        
    username = get_new_username(path)
    print(f"We'll remember you next time, {username}.")

greet_user()