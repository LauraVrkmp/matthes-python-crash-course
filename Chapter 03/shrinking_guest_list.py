guests = ["Abel", "Boaz", "Charlie", "Dennis"]

guests.insert(0, "Lola")
guests.insert(3, "Manson")
guests.append("Randell")

print(f"{guests[0]}, you are invited to dinner!")
print(f"{guests[1]}, you are invited to dinner!")
print(f"{guests[2]}, you are invited to dinner!")
print(f"{guests[3]}, you are invited to dinner!")
print(f"{guests[4]}, you are invited to dinner!")
print(f"{guests[5]}, you are invited to dinner!")
print(f"{guests[6]}, you are invited to dinner!")

print("\nI can invite only two people for dinner.")
removed_guest = guests.pop(1)
print(f"Sorry, I can't invite you {removed_guest}")
removed_guest = guests.pop(4)
print(f"Sorry, I can't invite you {removed_guest}")
removed_guest = guests.pop(2)
print(f"Sorry, I can't invite you {removed_guest}")
removed_guest = guests.pop(3)
print(f"Sorry, I can't invite you {removed_guest}")
removed_guest = guests.pop(0)
print(f"Sorry, I can't invite you {removed_guest}")

print(f"You're still invited, {guests[0]}.")
print(f"You're also still invited, {guests[1]}.")

del guests[0]
del guests[0]

print(guests)