from pathlib import Path

name = input("What's your name? ")
path = Path("Chapter 10/guest.txt")
path.write_text(name)