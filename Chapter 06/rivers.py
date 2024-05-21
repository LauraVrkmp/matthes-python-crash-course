rivers = {"nile": "egypt", "amstel": "the netherlands", "spree": "germany"}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"The river {river.title()} is included in the dictionary.")

for country in rivers.values():
    print(f"{country.title()} is included in the dictionary.")