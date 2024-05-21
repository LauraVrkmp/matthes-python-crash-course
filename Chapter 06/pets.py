pet_1 = {"kind": "bird", "owner": "Larry"}
pet_2 = {"kind": "lizard", "owner": "Ben"}
pet_3 = {"kind": "hamster", "owner": "Ashley"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"The animal is a {pet["kind"]}, it's owner is {pet["owner"]}.")
