dream_vacations = []

while True:
    dream_vacation = input("If you could visit one place in the "
                           "world, where would you go? ")
    if dream_vacation == 'quit':
        break
    else:
        dream_vacations.append(dream_vacation)

print("Results of the poll:")
for vacation in dream_vacations:
    print(f"- {vacation}")
