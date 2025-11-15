"""
Application composition root.

Creates shared singletons for storage and services so that all commands
work with the same data (contacts + notes) and persistent file.
"""

from src.storage import FileStore
from src.services import ContactsService, NotesService, BirthdayService, SearchService


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
