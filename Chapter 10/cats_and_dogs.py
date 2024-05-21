from pathlib import Path

filenames = ["Chapter 10/cats.txt", "Chapter 10/dogs.txt"]

for filename in filenames:
    print(f"Reading file {filename}")
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("The file was not found.")
    else:
        print(contents)