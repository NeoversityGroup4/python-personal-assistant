# Handles CRUD for notes:
#  - add(), delete(), find(), find_by_tags(), edit()
#  - each note may include one or more tags


# services/notes_service.py

# services/notes_service.py
from core.models.notes import Note

class NotesService:
    def __init__(self, store=None):
        """store: список Note або інше сховище (необов'язково)"""
        self.notes = store if store is not None else []

    def get_all(self):
        return self.notes

    def add(self, note):
        if not isinstance(note, Note):
            raise ValueError("Очікується об’єкт типу Note")
        self.notes.append(note)
        return note

    def update(self, note_id, **kwargs):
        note = self.find(note_id)
        if note:
            note.text = kwargs.get("text", note.text)
            note.tags = kwargs.get("tags", note.tags)
            return note
        return None

    def delete(self, note_id):
        note = self.find(note_id)
        if note:
            self.notes.remove(note)
            return True
        return False

    def find(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def find_by_tags(self, tags=None, text=None):
        results = self.notes
        if tags:
            tags_set = set(tag.lower() for tag in tags)
            results = [note for note in results if tags_set.intersection(t.lower() for t in note.tags)]
        if text:
            text_lower = text.lower()
            results = [note for note in results if text_lower in note.text.lower()]
        return results

