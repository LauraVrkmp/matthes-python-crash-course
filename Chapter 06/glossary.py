words = {
    "string": "a series of characters",
    "comment": "a note in a program that the Python interpreter ignores",
    "list": "a collection of items in a particular order",
    "loop": "work through a colleciton of items, one at a time",
    "dictionary": "a collection of key-value pairs",
    }

word = "string"
print(f"{word.title()}: {words[word]}")
word = 'comment'
print(f"\n{word.title()}: {words[word]}")
word = 'list'
print(f"\n{word.title()}: {words[word]}")
word = 'loop'
print(f"\n{word.title()}: {words[word]}")
word = 'dictionary'
print(f"\n{word.title()}: {words[word]}")