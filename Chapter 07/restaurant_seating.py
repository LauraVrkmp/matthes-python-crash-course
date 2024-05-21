group = input("With how many people would you like to have dinner? ")
group = int(group)

if group > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")