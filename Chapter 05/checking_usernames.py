current_users = ["Webber", "Dolittle101", "Admin", "Scabbart", "Bandit"]
new_users = ["Looper", "weBBer", "Lady", "Whackoo", "Snoozer"]

current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Enter a new username")
    else:
        print("The username is available")