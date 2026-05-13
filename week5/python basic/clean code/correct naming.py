def get_active_adults(users):
    active_user_names = []
    for name, age, is_active in users:
        if age >= 18 and is_active:
            active_user_names.append(name)
    return active_user_names

users_data = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]

print(get_active_adults(users_data))
