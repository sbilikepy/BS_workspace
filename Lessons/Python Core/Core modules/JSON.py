import json  # JavaScript object notation

with open("some.json") as f:
    try:
        user_data = json.load(f)
        print(user_data)
        print(type(user_data))
    except Exception as e:
        print(e)

user_data.append({
    "users_data_new": {
        "name": "Sanya",
        "surname": "Smo",
        "age": 25
    }
})
print(user_data)

with open("some.json", "w") as f:
    json.dump(user_data, f, indent=2)  # format


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user_data.append(User(
    name="Anna",
    surname="White",
    age=33
))
print(user_data)
with open("some.json", "w") as f:
    json.dump(user_data,f, indent=2)