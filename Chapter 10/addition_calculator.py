print("This program adds numbers.")

sum = 0
while True:
    new_number = input("Enter a number: ")
    if new_number == 'q':
        break
    try:
        sum += int(new_number)
    except ValueError:
        print("The entered value was not a number.")
    else:
        print(f"The total is {sum}.")