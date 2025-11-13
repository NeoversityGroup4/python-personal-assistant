from ..services.search_service import SearchService

class SearchCommand:
    def __init__(self):
        self.service = SearchService()
    
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
            
            return "\n".join(output)
            
        except Exception as e:
            return f"Помилка при пошуку: {str(e)}"
    
    def help(self):
        return "Використання: search <запит> - глобальний пошук по контактах та нотатках"