def sort_names(names: list) -> list:
    return sorted(names)[:3:]


def get_uppercase_string(source_strings: list) -> list:
    return [i.upper() for i in source_strings if len(i) and i[0] in ("a", "b") and len(i) >= 3]


def pretty_list(numbers: list) -> bool:
    if len(numbers):
        for num in numbers:
            if not isinstance(num, (int, float)):
                return False
            if not (num - 1 in numbers or num + 1 in numbers):
                return False
        return True
    return False


def sum_of_segments(segments: str) -> int:
    segments = sorted(segments)
    result = 0
    current_end = float("-inf")

    for start, end in segments:
        if start > current_end:
            result += end - start
            current_end = end
        elif end > current_end:
            result += end - current_end
            current_end = end

    return result


class User:
    def __init__(self,
                 email: str,
                 username: str,
                 last_activity: str,
                 is_online: bool) -> None:
        self.email = email
        self.username = username
        self.last_activity = last_activity
        self.is_online = is_online


def update_users_status(users: list[User]) -> None:
    for user in users:
        if user.is_online:
            if user.last_activity.split()[1] != "minutes":
                user.is_online = False
                print(f"{user.username} became offline")
            elif int(user.last_activity.split()[0]) >= 15:
                user.is_online = False
                print(f"{user.username} became offline")
        else:
            if user.last_activity.split()[1] == "minutes":
                if int(user.last_activity.split()[0]) < 15:
                    user.is_online = True
                    print(f"{user.username} became online")


class Matrix:
    def __init__(self, elements: list) -> None:
        for i in elements:
            if not len(i) == len(elements):
                raise ValueError
        self.matrix = elements

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError
        if len(self.matrix) != len(other.matrix):
            raise ValueError
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return Matrix(result)
