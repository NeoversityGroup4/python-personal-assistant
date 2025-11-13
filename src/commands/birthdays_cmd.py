# CLI command for birthday listing:
#  - upcoming --in N
#  - prints people with birthdays within N days

from ..services.birthday_service import BirthdayService

class BirthdaysCommand:
    def __init__(self):
        self.service = BirthdayService()
    
    def upcoming(self, days):
        try:
            days_int = int(days)
            if days_int < 0:
                return "Помилка: Кількість днів має бути додатним числом"
            
            upcoming_birthdays = self.service.get_upcoming_birthdays(days_int)
            
            if not upcoming_birthdays:
                return f"Не знайдено контактів з днями народження протягом наступних {days_int} днів"
            
            result = [f"Контакти з днями народження протягом наступних {days_int} днів:"]
            for contact in upcoming_birthdays:
                result.append(f"- {contact.name}: {contact.birthday}")
            
            return "\n".join(result)
            
        except ValueError:
            return "Помилка: Кількість днів має бути числом"
        except Exception as e:
            return f"Помилка при пошуку днів народження: {str(e)}"