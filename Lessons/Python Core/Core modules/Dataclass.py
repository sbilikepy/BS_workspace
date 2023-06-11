import dataclasses


@dataclasses.dataclass
class User:
    name: str
    surname: str
    age: int


x = User(name="Sa", surname="Bo", age=34)
print(x.__dict__)
print(type(x))
