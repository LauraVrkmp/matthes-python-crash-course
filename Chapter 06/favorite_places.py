favorite_places = {"Ben": ["Disney", "park", "mall"],
                   "Ashley": ["mall", "beach"],
                   "Tom": ["lake"]
                   }

for name, places in favorite_places.items():
    print(f"{name} likes to go to:")
    for place in places:
        print(f"- {place}")