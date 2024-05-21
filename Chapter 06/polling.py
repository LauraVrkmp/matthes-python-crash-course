favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

should_take = ["david", "barbara", "phil", "edward"]

for name in should_take:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for polling!")
    else:
        print(f"{name.title()}, we invite you to take the poll!")