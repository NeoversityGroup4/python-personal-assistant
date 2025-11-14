from ..services.search_service import SearchService

class SearchCommand:
    def __init__(self):
        self.service = SearchService()
    
<<<<<<< HEAD
    def global_search(self, query):
        try:
            if not query or not query.strip():
                return "Error: Please enter search query"
            
            results = self.service.search_all(query.strip())
            
            if not results['contacts'] and not results['notes']:
                return f"Nothing found for query '{query}'"
            
            output = []
            
            if results['contacts']:
                output.append("=== CONTACTS ===")
                for contact in results['contacts']:
                    output.append(f"Name: {contact.name}")
                    if contact.phone:
                        output.append(f"  Phone: {contact.phone}")
                    if contact.email:
                        output.append(f"  Email: {contact.email}")
                    if contact.birthday:
                        output.append(f"  Birthday: {contact.birthday}")
                    output.append("")
            
            if results['notes']:
                output.append("=== NOTES ===")
                for note in results['notes']:
                    output.append(f"Note: {note.text[:100]}{'...' if len(note.text) > 100 else ''}")
                    if note.tags:
                        output.append(f"  Tags: {', '.join(note.tags)}")
                    output.append("")
=======
    def global_search(self, query):# Глобальний пошук по ключовому слову в контактах та нотатках
        try:
            if not query or not query.strip():
                return "Помилка-> Введіть пошуковий запит"
            
            results = self.service.search_all(query.strip())
    
            if not results['contacts'] and not results['notes']:
                return f"За запитом '{query}' нічого не знайдено"
            
            output = []
        
            if results['contacts']:
                output.append("=== КОНТАКТИ ===")
                for contact in results['contacts']:
                    output.append(f" {contact.name}")
                    if contact.phone:
                        output.append(f"   Телефон: {contact.phone}")
                    if contact.email:
                        output.append(f"   Email: {contact.email}")
                    if contact.birthday:
                        output.append(f"   День народження: {contact.birthday}")
                    output.append("")  # пустий рядок між контактами
            
            # Результати по нотаткам
            if results['notes']:
                output.append("=== НОТАТКИ ===")
                for note in results['notes']:
                    output.append(f" Нотатка: {note.text[:100]}{'...' if len(note.text) > 100 else ''}")
                    if note.tags:
                        output.append(f"   Теги: {', '.join(note.tags)}")
                    output.append("")  # пустий рядок між нотатками
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
            
            return "\n".join(output)
            
        except Exception as e:
<<<<<<< HEAD
            return f"Error during search: {str(e)}"
    
    def help(self):
        return "Usage: search <query> - global search across contacts and notes"
=======
            return f"Помилка при пошуку: {str(e)}"
    
    def help(self):
        return "Використання: search <запит> - глобальний пошук по контактах та нотатках"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
