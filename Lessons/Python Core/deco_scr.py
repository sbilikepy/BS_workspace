from typing import Callable


def arrow(func: Callable) -> None:
    def wrapper(items: dict) -> None:
        new_format_items = [f"{key} -> {value}" for key, value in items.items()]
        return func(new_format_items)

    return wrapper


def number_filter(func: Callable) -> None:
    def wrapper(items: list) -> None:
        new_format_items = [num for num in items if isinstance(num, (int, float))]
        return func(new_format_items)

    return wrapper


def round_dict(func: Callable) -> None:
    def wrapper(items: list) -> None:
        new_format_items = {round(item): round(item) * 2 for item in items}
        return func(new_format_items)

    return wrapper


@number_filter
@round_dict
@arrow
def like_numbers(items: list) -> str:
    return f"I like to filter, rounding, doubling, store and decorate numbers: {', '.join(items)}!"


items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]
print(like_numbers(items))
