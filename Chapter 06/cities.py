cities = {
    "Warsaw": {
        "country": "Poland",
        "population": "1.8 million",
        "fact": "been there"
        },
    "Paris": {
        "country": "France",
        "population": "2.2 million",
        "fact": "on the river Seine"
        },
    "Amsterdam": {
        "country": "The Netherlands",
        "population": "0.8 million",
        "fact": "live there"
        }
    }

for city, info in cities.items():
    print(f"Some information about {city}:")
    print(f"It's in {info["country"]}, "
          f"it's population is {info["population"]}, "
          f"and one fact: {info["fact"]}.")