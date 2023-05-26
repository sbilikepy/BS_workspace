import time


def delay(seconds: int,
          func):
    time.sleep(seconds)
    return func()


def get_data():
    return {"data": "json"}


def print_hello_world():
    print("Hello world!")


if __name__ == '__main__':
    print(delay(3, get_data()))  # {"data":"json"}
    delay(2, print_hello_world())  # prints:"Hello world!"
