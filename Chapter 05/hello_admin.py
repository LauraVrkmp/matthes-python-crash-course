usernames = ["webber", "dolittle101", "admin", "scabbart", "bandit"]

for username in usernames:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for loggin in again.")