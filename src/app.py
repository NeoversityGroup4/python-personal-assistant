"""
Application composition root.

Creates shared singletons for storage and services so that all commands
work with the same data (contacts + notes) and persistent file.
"""

from src.storage.file_store import FileStore
from src.services.contacts_service import ContactsService
from src.services.notes_service import NotesService
from src.services.birthday_service import BirthdayService
from src.services.search_service import SearchService


# Single store instance for the whole app
store = FileStore()

# Singleton services
contacts_service = ContactsService(store)
notes_service = NotesService(store)
birthdays_service = BirthdayService(store)
search_service = SearchService(contacts_service, notes_service)


__all__ = [
    "store",
    "contacts_service",
    "notes_service",
    "birthdays_service",
    "search_service",
]
