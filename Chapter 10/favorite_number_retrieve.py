from pathlib import Path
import json

input = "Chapter 10/favorite_number.json"
path = Path(input)
contents = path.read_text()
favorite_number = json.loads(contents)
print(f"Your favorite number is {favorite_number}.")