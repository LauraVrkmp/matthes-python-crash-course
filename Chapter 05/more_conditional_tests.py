dog = "Mimo"
print("Is dog == \"Mimo\"? I predict True.")
print(dog == "Mimo")

print("Is dog == \"Geezer\"? I predict False.")
print(dog == "Geezer")

print(dog.lower() == "mimo")

number = 5
print(number == 4)
print(number != 6)
print(number > 3)
if number and dog:
    print("Number and dog are defined.")

items = ["jaccuzzi", "pool", "pond"]

if "ocean" in items:
    print("Is in items.")
else:
    print("Is not in items.")