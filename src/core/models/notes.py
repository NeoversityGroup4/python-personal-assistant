# Defines the Note class:
#  - attributes: text, list of tags
#  - helper methods: __str__(), to_dict(), from_dict()


class Tag:
    pass


class Note:
    def __init__(self, note_id: int, text: str, tags=None):
        """
        Ініціалізація нотатки.
        :param note_id: унікальний ідентифікатор
        :param text: текст нотатки
        :param tags: список тегів (опціонально)
        """
        self.id = note_id
        self.text = text
        self.tags = tags or []

    def to_dict(self) -> dict:
        """Повертає словник для збереження у файл або JSON."""
        return {
            "id": self.id,
            "text": self.text,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Створює Note з словника."""
        return cls(
            note_id=data.get("id"),
            text=data.get("text", ""),
            tags=data.get("tags", [])
        )

    def __str__(self):
        """Красиве відображення нотатки для CLI."""
        tags_str = ", ".join(self.tags) if self.tags else "No tags"
        return f"Note[{self.id}]: {self.text} | Tags: {tags_str}"

# Note model implemented by Antonina

