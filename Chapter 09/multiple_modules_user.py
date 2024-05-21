class User:
    def __init__(self, first_name, last_name, username, active):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.active = active
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user {self.username} is called {self.first_name} "
              f"{self.last_name}, and has been active for {self.active} years.")
    
    def greet_user(self):
        print(f"Welcome to the forum, {self.username}.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0