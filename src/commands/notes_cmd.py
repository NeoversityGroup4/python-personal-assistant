from ..services.notes_service import NotesService

class NotesCommand:
<<<<<<< HEAD
    # Constants for text truncation
    SEARCH_RESULT_TRUNCATE = 80
    LIST_RESULT_TRUNCATE = 60
    GLOBAL_SEARCH_TRUNCATE = 100
    
    def __init__(self):
        self.service = NotesService()
    
    def add_note(self, text, tags=None):
        try:
            if not text or not text.strip():
                return "Error: Note text cannot be empty"
            
            result = self.service.add_note(text.strip(), tags)
            tag_info = f" with tags: {', '.join(tags)}" if tags else ""
            return f"Note successfully added! (ID: {result.id}){tag_info}"
        except Exception as e:
            return f"Error adding note: {str(e)}"
=======
    def __init__(self):
        self.service = NotesService()
    
    def add_note(self, text, tags=None): #Додавання нового нотатку
        try:
            if not text or not text.strip():
                return "Помилка: Текст нотатки не може бути порожнім"
            
            result = self.service.add_note(text.strip(), tags)
            tag_info = f" з тегами: {', '.join(tags)}" if tags else ""
            return f"Нотатку успішно додано! (ID: {result.id}){tag_info}"
        except Exception as e:
            return f" Помилка при додаванні нотатки: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def edit_note(self, note_id, new_text=None, new_tags=None):
        try:
            result = self.service.edit_note(note_id, new_text, new_tags)
<<<<<<< HEAD
            return f"Note (ID: {note_id}) successfully updated!"
        except Exception as e:
            return f"Error editing note: {str(e)}"
    
    def delete_note(self, note_id):
        try:
            self.service.delete_note(note_id)
            return f"Note (ID: {note_id}) successfully deleted!"
        except Exception as e:
            return f"Error deleting note: {str(e)}"
=======
            return f"Нотатку (ID: {note_id}) успішно оновлено!"
        except Exception as e:
            return f"Помилка при редагуванні нотатки: {str(e)}"
    
    def delete_note(self, note_id): #Видалити нонаток
        try:
            self.service.delete_note(note_id)
            return f"Нотатку (ID: {note_id}) успішно видалено!"
        except Exception as e:
            return f"Помилка при видаленні нотатки: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def search_notes(self, query):
        try:
            results = self.service.search_notes(query)
            if not results:
<<<<<<< HEAD
                return f"No notes found for query '{query}'"
            
            output = ["Note search results:"]
            for note in results:
                truncated_text = self._truncate_text(note.text, self.SEARCH_RESULT_TRUNCATE)
                note_info = f"{truncated_text}"
                if note.tags:
                    note_info += f" | Tags: {', '.join(note.tags)}"
=======
                return f"Нотатки за запитом '{query}' не знайдено"
            
            output = ["Результати пошуку нотаток:"]
            for note in results:
                note_info = f"{note.text[:80]}{'...' if len(note.text) > 80 else ''}"
                if note.tags:
                    note_info += f" | {', '.join(note.tags)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
                note_info += f" | ID: {note.id}"
                output.append(note_info)
            
            return "\n".join(output)
        except Exception as e:
<<<<<<< HEAD
            return f"Error searching notes: {str(e)}"
=======
            return f"Помилка при пошуку нотаток: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def search_notes_by_tag(self, tag):
        try:
            results = self.service.search_by_tag(tag)
            if not results:
<<<<<<< HEAD
                return f"No notes found with tag '{tag}'"
            
            output = [f"Notes with tag '{tag}':"]
            for note in results:
                truncated_text = self._truncate_text(note.text, self.SEARCH_RESULT_TRUNCATE)
                note_info = f"{truncated_text}"
                if note.tags:
                    note_info += f" | Tags: {', '.join(note.tags)}"
=======
                return f"🔍 Нотатки з тегом '{tag}' не знайдено"
            
            output = [f"🔍 Нотатки з тегом '{tag}':"]
            for note in results:
                note_info = f"{note.text[:80]}{'...' if len(note.text) > 80 else ''}"
                if note.tags:
                    note_info += f" | {', '.join(note.tags)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
                note_info += f" | ID: {note.id}"
                output.append(note_info)
            
            return "\n".join(output)
        except Exception as e:
<<<<<<< HEAD
            return f"Error searching by tag: {str(e)}"
=======
            return f"Помилка при пошуку за тегом: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def list_notes(self):
        try:
            notes = self.service.get_all_notes()
            if not notes:
<<<<<<< HEAD
                return "Note list is empty"
            
            output = ["All notes:"]
            for note in notes:
                truncated_text = self._truncate_text(note.text, self.LIST_RESULT_TRUNCATE)
                note_info = f"{truncated_text}"
                if note.tags:
                    note_info += f" | Tags: {', '.join(note.tags)}"
=======
                return "Список нотаток порожній"
            
            output = ["Список всіх нотаток:"]
            for note in notes:
                note_info = f"{note.text[:60]}{'...' if len(note.text) > 60 else ''}"
                if note.tags:
                    note_info += f" | {', '.join(note.tags)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
                note_info += f" | ID: {note.id}"
                output.append(note_info)
            
            return "\n".join(output)
        except Exception as e:
<<<<<<< HEAD
            return f"Error getting note list: {str(e)}"
    
    def _truncate_text(self, text, max_length):
        if len(text) <= max_length:
            return text
        return text[:max_length] + '...'
=======
            return f"Помилка при отриманні списку нотаток: {str(e)}"
    
    def add_tags(self, note_id, tags):
        try:
            result = self.service.add_tags(note_id, tags)
            return f"Теги успішно додано до нотатки (ID: {note_id}): {', '.join(tags)}"
        except Exception as e:
            return f"Помилка при додаванні тегів: {str(e)}"
    
    def remove_tags(self, note_id, tags):
        """Видалити теги з нотатки"""
        try:
            result = self.service.remove_tags(note_id, tags)
            return f"Теги успішно видалено з нотатки (ID: {note_id}): {', '.join(tags)}"
        except Exception as e:
            return f"Помилка при видаленні тегів: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
