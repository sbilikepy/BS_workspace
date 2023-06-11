import pickle



class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


users = [
    User(name="Jo", surname="Bi", age=100),
    User(name="Ro", surname="Bi", age=132)
]

with open("data.pickle", "wb") as f: #binary write "wb"
    pickle.dump(users, f)


del users


with open("data.pickle", "rb") as f: #read binary "rb"
    users = pickle.load(f)
    print(users)

for _ in users:
    print(_.name)
