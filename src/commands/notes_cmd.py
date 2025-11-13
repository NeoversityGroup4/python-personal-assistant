from ..services.notes_service import NotesService

class NotesCommand:
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
    
    def edit_note(self, note_id, new_text=None, new_tags=None):
        try:
            result = self.service.edit_note(note_id, new_text, new_tags)
            return f"Нотатку (ID: {note_id}) успішно оновлено!"
        except Exception as e:
            return f"Помилка при редагуванні нотатки: {str(e)}"
    
    def delete_note(self, note_id): #Видалити нонаток
        try:
            self.service.delete_note(note_id)
            return f"Нотатку (ID: {note_id}) успішно видалено!"
        except Exception as e:
            return f"Помилка при видаленні нотатки: {str(e)}"
    
    def search_notes(self, query):
        try:
            results = self.service.search_notes(query)
            if not results:
                return f"Нотатки за запитом '{query}' не знайдено"
            
            output = ["Результати пошуку нотаток:"]
            for note in results:
                note_info = f"{note.text[:80]}{'...' if len(note.text) > 80 else ''}"
                if note.tags:
                    note_info += f" | {', '.join(note.tags)}"
                note_info += f" | ID: {note.id}"
                output.append(note_info)
            
            return "\n".join(output)
        except Exception as e:
            return f"Помилка при пошуку нотаток: {str(e)}"
    
    def search_notes_by_tag(self, tag):
        try:
            results = self.service.search_by_tag(tag)
            if not results:
                return f"🔍 Нотатки з тегом '{tag}' не знайдено"
            
            output = [f"🔍 Нотатки з тегом '{tag}':"]
            for note in results:
                note_info = f"{note.text[:80]}{'...' if len(note.text) > 80 else ''}"
                if note.tags:
                    note_info += f" | {', '.join(note.tags)}"
                note_info += f" | ID: {note.id}"
                output.append(note_info)
            
            return "\n".join(output)
        except Exception as e:
            return f"Помилка при пошуку за тегом: {str(e)}"
    
    def list_notes(self):
        try:
            notes = self.service.get_all_notes()
            if not notes:
                return "Список нотаток порожній"
            
            output = ["Список всіх нотаток:"]
            for note in notes:
                note_info = f"{note.text[:60]}{'...' if len(note.text) > 60 else ''}"
                if note.tags:
                    note_info += f" | {', '.join(note.tags)}"
                note_info += f" | ID: {note.id}"
                output.append(note_info)
            
            return "\n".join(output)
        except Exception as e:
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