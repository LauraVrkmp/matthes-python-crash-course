def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Laura', 'Veerkamp',
                             location='Amsterdam',
                             profession='student',
                             interest='programming')

print(user_profile)