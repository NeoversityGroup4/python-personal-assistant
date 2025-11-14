from ..services.contacts_service import ContactsService

class ContactsCommand:
    def __init__(self):
        self.service = ContactsService()
    
    def add_contact(self, name, phone=None, email=None, address=None, birthday=None):
        try:
            result = self.service.add_contact(name, phone, email, address, birthday)
<<<<<<< HEAD
            return f"Contact '{name}' successfully added! (ID: {result.id})"
        except Exception as e:
            return f"Error adding contact: {str(e)}"
=======
            return f" Контакт '{name}' успішно додано! (ID: {result.id})"
        except Exception as e:
            return f" Помилка при додаванні контакту: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def edit_contact(self, contact_id, **kwargs):
        try:
            result = self.service.edit_contact(contact_id, **kwargs)
<<<<<<< HEAD
            return f"Contact '{result.name}' successfully updated!"
        except Exception as e:
            return f"Error editing contact: {str(e)}"
=======
            return f" Контакт '{result.name}' успішно оновлено!"
        except Exception as e:
            return f" Помилка при редагуванні контакту: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def delete_contact(self, contact_id):
        try:
            contact_name = self.service.get_contact(contact_id).name
            self.service.delete_contact(contact_id)
<<<<<<< HEAD
            return f"Contact '{contact_name}' successfully deleted!"
        except Exception as e:
            return f"Error deleting contact: {str(e)}"
=======
            return f" Контакт '{contact_name}' успішно видалено!"
        except Exception as e:
            return f" Помилка при видаленні контакту: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def search_contacts(self, query):
        try:
            results = self.service.search_contacts(query)
            if not results:
<<<<<<< HEAD
                return f"No contacts found for query '{query}'"
            
            output = ["Contact search results:"]
            for contact in results:
                contact_info = f"{contact.name}"
                if contact.phone:
                    contact_info += f" | Phone: {contact.phone}"
                if contact.email:
                    contact_info += f" | Email: {contact.email}"
                if contact.birthday:
                    contact_info += f" | Birthday: {contact.birthday}"
=======
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
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
                output.append(contact_info)
            
            return "\n".join(output)
        except Exception as e:
<<<<<<< HEAD
            return f"Error during search: {str(e)}"
=======
            return f" Помилка при пошуку: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
    
    def list_contacts(self):
        try:
            contacts = self.service.get_all_contacts()
            if not contacts:
<<<<<<< HEAD
                return "Contact list is empty"
            
            output = ["All contacts:"]
            for i, contact in enumerate(contacts, 1):
                contact_info = f"{i}. {contact.name}"
                if contact.phone:
                    contact_info += f" | Phone: {contact.phone}"
                if contact.email:
                    contact_info += f" | Email: {contact.email}"
                if contact.birthday:
                    contact_info += f" | Birthday: {contact.birthday}"
=======
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
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
                output.append(contact_info)
            
            return "\n".join(output)
        except Exception as e:
<<<<<<< HEAD
            return f"Error getting contact list: {str(e)}"
=======
            return f" Помилка при отриманні списку контактів: {str(e)}"
    
    def get_contact(self, contact_id):
        try:
            return self.service.get_contact(contact_id)
        except Exception as e:
            return f" Помилка при отриманні контакту: {str(e)}"
>>>>>>> 4d26b9fa1c0c853cf16302b138e2002d49caac76
