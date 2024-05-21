person_1 = {"first_name": "Laura", "last_name": "Veerkamp",
           "age": 30, "city": "Amsterdam"}
person_2 = {"first_name": "Kevin", "last_name": "Steward",
            "age": 24, "city": "Belfast"}
person_3 = {"first_name": "Lisa", "last_name": "Lowees",
             "age": 45, "city": "Berlin"}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Their first name is {person["first_name"]}, "
        f"their last name is {person["last_name"]}, "
        f"their age is {person["age"]} "
        f"and their location is {person["city"]}")