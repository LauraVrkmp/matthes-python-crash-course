class User:
    def __init__(self, first_name, last_name, username, active):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.active = active

    def describe_user(self):
        print(f"The user {self.username} is called {self.first_name} "
              f"{self.last_name}, and has been active for {self.active} years.")
    
    def greet_user(self):
        print(f"Welcome to the forum, {self.username}.")

user_1 = User("Laura", "Veerkamp", "lveerkamp", 3)
user_2 = User("Kim", "Putters", "kputters", 2)
user_3 = User("Layla", "Roosen", "lroosen", 4)

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()