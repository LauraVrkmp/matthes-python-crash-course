sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich")

print("All the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
