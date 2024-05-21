print("This program adds two numbers.")
num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

try:
    sum = int(num_1) + int(num_2)
except ValueError:
    print("The input did not consist of two numbers.")
else:
    print(f"The sum is {sum}.")