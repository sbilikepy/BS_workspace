import sqlite3

from models import LiteraryFormat


class LiteraryFormatManager:
    def __init__(self):
        self._connection = sqlite3.connect("library_db")
        self.table_name = "literary_formats"

    # CRUD:
    # CREATE C
    def create(self, format_: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)", (format_,)
        )
        self._connection.commit()

    # RETRIEVE (READ)
    def all(self):
        literary_formats_cursor = self._connection.execute(
            f"SELECT id, format FROM {self.table_name}"
        )

        return [LiteraryFormat(*row) for row in literary_formats_cursor]

    # UPDATE U
    def update(self, id_to_update, new_format):
        self._connection.execute(
            f"UPDATE {self.table_name} " "SET format = ? " "WHERE id = ?",
            (new_format, id_to_update),
        )
        self._connection.commit()

    # DELETE D
    def delete(self, id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.table_name} " f"WHERE id =  ?", (id_to_delete,)
        )
        self._connection.commit()


# if __name__ == "__main__":
#     manager = LiteraryFormatManager()
#     manager.update(id_to_update=5, new_format='prose')
#     manager.delete(8)
#     print(manager.all())
