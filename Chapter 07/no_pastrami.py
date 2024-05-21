sandwich_orders = ['veggie', 'pastrami', 'pastrami', 'grilled cheese', 
                   'turkey', 'roast beef', 'pastrami']

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich")

print("All the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")