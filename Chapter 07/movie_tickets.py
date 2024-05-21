while True:
    age = input("Enter your age: ")

    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age < 13:
        print("You pay $10.")
    else:
        print("You pay $15.")