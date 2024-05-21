from pathlib import Path

name = ''
while True:
    new_name = input("What's your name? ")
    if new_name == 'q':
        break
    name += new_name
    name += '\n'

path = Path("Chapter 10/guest_book.txt")
path.write_text(name)