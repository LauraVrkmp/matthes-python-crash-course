active = True
while active:
    age = input("Enter your age: ")

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age < 13:
            print("You pay $10.")
        else:
            print("You pay $15.")