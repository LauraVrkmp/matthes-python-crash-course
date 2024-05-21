from pathlib import Path
import json

favorite_number = input("What's your favorite number? ")

output = "Chapter 10/favorite_number.json"
path = Path(output)
contents = json.dumps(favorite_number)
path.write_text(contents)
print(f"Wrote {favorite_number} to {path}.")