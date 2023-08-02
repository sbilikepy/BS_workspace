class LiteraryFormat:
    def __init__(self, id_from_db: int, genre: str):
        self.id = id_from_db
        self.format = genre

    def __repr__(self):
        return (f"LiteraryFormat(id={self.id} "
                f"format={self.format})")
