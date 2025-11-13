from ..services.contacts_service import ContactsService

class ContactsCommand:
    def __init__(self):
        self.service = ContactsService()
    
    def add_contact(self, name, phone=None, email=None, address=None, birthday=None):
        try:
            result = self.service.add_contact(name, phone, email, address, birthday)
            return f" Контакт '{name}' успішно додано! (ID: {result.id})"
        except Exception as e:
            return f" Помилка при додаванні контакту: {str(e)}"
    
    def edit_contact(self, contact_id, **kwargs):
        try:
            result = self.service.edit_contact(contact_id, **kwargs)
            return f" Контакт '{result.name}' успішно оновлено!"
        except Exception as e:
            return f" Помилка при редагуванні контакту: {str(e)}"
    
    def delete_contact(self, contact_id):
        try:
            contact_name = self.service.get_contact(contact_id).name
            self.service.delete_contact(contact_id)
            return f" Контакт '{contact_name}' успішно видалено!"
        except Exception as e:
            return f" Помилка при видаленні контакту: {str(e)}"
    
    def search_contacts(self, query):
        try:
            results = self.service.search_contacts(query)
            if not results:
                return f" Контакти за запитом '{query}' не знайдено"
            
            output = [" Результати пошуку контактів:"]
            for contact in results:
                contact_info = f" {contact.name}"
                if contact.phone:
                    contact_info += f" |  {contact.phone}"
                if contact.email:
                    contact_info += f" |  {contact.email}"
                if contact.birthday:
                    contact_info += f" |  {contact.birthday}"
                output.append(contact_info)
            
            return "\n".join(output)
        except Exception as e:
            return f" Помилка при пошуку: {str(e)}"
    
    def list_contacts(self):
        try:
            contacts = self.service.get_all_contacts()
            if not contacts:
                return " Список контактів порожній"
            
            output = [" Список всіх контактів:"]
            for i, contact in enumerate(contacts, 1):
                contact_info = f"{i}. {contact.name}"
                if contact.phone:
                    contact_info += f" |  {contact.phone}"
                if contact.email:
                    contact_info += f" |  {contact.email}"
                if contact.birthday:
                    contact_info += f" |  {contact.birthday}"
                output.append(contact_info)
            
            return "\n".join(output)
        except Exception as e:
            return f" Помилка при отриманні списку контактів: {str(e)}"
    
    def get_contact(self, contact_id):
        try:
            return self.service.get_contact(contact_id)
        except Exception as e:
            return f" Помилка при отриманні контакту: {str(e)}"