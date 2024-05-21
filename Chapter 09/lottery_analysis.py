from random import randint

series = [4, 3, 0, 8, 3, 7, 6, 2, 7, 1, 'l', 'o', 'q', 'v', 'o']

my_ticket = "83q1"
count = 0

while True:
    count += 1
    winning = ""
    for i in range(4):
        pick = series[randint(0, len(series) - 1)]
        winning += str(pick)
    
    if my_ticket == winning:
        print(f"You won! Your ticket {my_ticket} is the same as "
              f"the winning ticket {winning}!")
        print(f"It took {count} tries.")
        break