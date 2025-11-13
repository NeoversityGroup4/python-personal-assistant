# Defines the Note class:
#  - attributes: text, list of tags
#  - helper methods: __str__(), to_dict(), from_dict()


class Tag:
    pass


class Note:
    def __init__(self, note_id: int, text: str, tags=None):
        """
        Initialize a note.
        :param note_id: unique identifier
        :param text: note text
        :param tags: list of tags (optional)
        """
        self.id = note_id
        self.text = text
        self.tags = tags or []

    def to_dict(self) -> dict:
        """Returns a dictionary for saving to a file or JSON."""
        return {
            "id": self.id,
            "text": self.text,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a Note from a dictionary."""
        return cls(
            note_id=data.get("id"),
            text=data.get("text", ""),
            tags=data.get("tags", [])
        )

    def __str__(self):
        """Nicely formatted note display for CLI."""
        tags_str = ", ".join(self.tags) if self.tags else "No tags"
        return f"Note[{self.id}]: {self.text} | Tags: {tags_str}"


