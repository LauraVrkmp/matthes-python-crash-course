pizzas = ["margarita", "tartufo", "salmone"]

friend_pizzas = pizzas[:]
pizzas.append("tuna")
friend_pizzas.append("funghi")

print("My favorite pizza's are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)