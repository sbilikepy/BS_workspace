greeting = "Hello from the global scope"  # вне классов


def greet():
    greeting = "Hello from enclosing scope"  # считается такой, только в ней еще одна вложенная функция

    def nested():
        greeting = "Hello from local scope"
        print(greeting)

    nested()


greet()
print(greeting)
print("_________________________________")


greeting = "global"


def greet(greeting):
    print(f"greet in funk {greeting}")

    greeting = "hELLO FROM ENCLOSING SCOPE"

    print(f"greet in func:{greeting}")

    def nested():
        greeting = "local"
        print(greeting)

    nested()


greet("test")
print(greeting)


print(
    "________________global greeting_________________"
)  # начиная с этог места = работа с переменной
# из глобального цикла

greeting = "global"


def greet():
    global greeting
    print(f"greet in funk {greeting}")

    greeting = "hELLO FROM ENCLOSING SCOPE"

    print(f"greet in func:{greeting}")

    def nested():
        greeting = "local"
        print(greeting)

    nested()


greet()
print(greeting)
