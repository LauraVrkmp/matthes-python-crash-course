from pathlib import Path

filenames = ["Chapter 10/a_room_with_a_view.txt", "Chapter 10/metamorphosis.txt",
         "Chapter 10/romeo_and_juliet.txt"]

for filename in filenames:
    print(f"Counting words in {filename}.")
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"This file {path} was not found.")
    else:
        count = contents.lower().count('the')
        count_space = contents.lower().count('the ')
        print(f"'the' was found {count} times.")
        print(f"'the ' was found {count_space} times.")