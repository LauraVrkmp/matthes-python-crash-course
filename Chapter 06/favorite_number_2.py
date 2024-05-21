favorite_numbers = {"Katy": [28, 12], "Lennart": [1], "Dary": [60, 17, 33],
                    "Pearson": [14], "Timothy": [44, 16]
                    }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"{name} likes the numbers:")
    else:
        print(f"{name} like the number:")
    for number in numbers:
        print(f"- {number}")