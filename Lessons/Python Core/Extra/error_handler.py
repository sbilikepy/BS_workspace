from typing import Any, Callable


def error_handler(
    error_type: Exception,
    callback: Callable,
    *callback_args,
    **callback_kwargs
) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except error_type:
                return callback(*callback_args, **callback_kwargs)
        return inner
    return wrapper


def func_produce_value_error() -> int:
    print("Hello, ValueError")
    return int("0.2")


@error_handler(ValueError, lambda: "Bye, errors")
@error_handler(TypeError, func_produce_value_error)
def func_produce_type_error() -> str:
    print("Hello, TypeError")
    return 10 + "10"
