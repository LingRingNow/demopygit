def person (name, **data):
    print(name)
    print(data.items())
    for key, value in data.items():
        print(key, value)

person('John', age=27, loc='maba', phone=8291834)