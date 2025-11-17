from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
from __future__ import annotations 
from src.services.contacts_service import ContactsService
from src.services.notes_service import NotesService


class EntityType(Enum):
    CONTACT = "contact"
    NOTE = "note"


@dataclass
class SearchHit:

    entity_type: EntityType
    entity_id: Any
    preview: str
    relevance_score: float = 1.0


class SearchService:

    def __init__(self, contacts: ContactsService, notes: NotesService):
        self.contacts = contacts
        self.notes = notes

    def search_all(self, query: str) -> List[SearchHit]:

        if not query or not query.strip():
            return []

        query = query.strip().lower()
        results = []

        # Search in contacts
        contact_results = self.contacts.search(query=query)
        for contact in contact_results:
            preview = self._create_contact_preview(contact)
            score = self._calculate_relevance(contact, query, EntityType.CONTACT)
            results.append(SearchHit(
                entity_type=EntityType.CONTACT,
                entity_id=contact.id,
                preview=preview,
                relevance_score=score
            ))

        # Search in notes
        note_results = self.notes.find_by_tags(text=query)
        for note in note_results:
            preview = self._create_note_preview(note, query)
            score = self._calculate_relevance(note, query, EntityType.NOTE)
            results.append(SearchHit(
                entity_type=EntityType.NOTE,
                entity_id=note.id,
                preview=preview,
                relevance_score=score
            ))

        # Sort by relevance score (higher first)
        return sorted(results, key=lambda x: x.relevance_score, reverse=True)

    def search_by_type(self, query: str, entity_type: EntityType) -> List[SearchHit]:
        if not query or not query.strip():
            return []

        query = query.strip().lower()
        results = []

        if entity_type == EntityType.CONTACT:
            contact_results = self.contacts.search(query=query)
            for contact in contact_results:
                preview = self._create_contact_preview(contact)
                score = self._calculate_relevance(contact, query, entity_type)
                results.append(SearchHit(
                    entity_type=entity_type,
                    entity_id=contact.id,
                    preview=preview,
                    relevance_score=score
                ))

        elif entity_type == EntityType.NOTE:
            note_results = self.notes.find_by_tags(text=query)
            for note in note_results:
                preview = self._create_note_preview(note, query)
                score = self._calculate_relevance(note, query, entity_type)
                results.append(SearchHit(
                    entity_type=entity_type,
                    entity_id=note.id,
                    preview=preview,
                    relevance_score=score
                ))

        return sorted(results, key=lambda x: x.relevance_score, reverse=True)

    def _create_contact_preview(self, contact) -> str:
        preview_parts = [f"Contact: {contact.name.value}"]
        
        if contact.phone and contact.phone.value:
            preview_parts.append(f"📞 {contact.phone.value}")
        if contact.email and contact.email.value:
            preview_parts.append(f"✉️ {contact.email.value}")
        
        return " | ".join(preview_parts)

    def _create_note_preview(self, note, query: str) -> str:
        # Truncate note text for preview
        text = note.text
        if len(text) > 100:
            text = text[:97] + "..."
        
        preview = f"Note: {text}"
        
        # Add tags if present
        if note.tags:
            preview += f" [Tags: {', '.join(note.tags)}]"
            
        return preview

    def _calculate_relevance(self, entity, query: str, entity_type: EntityType) -> float:
 
        score = 1.0
        query = query.lower()

        if entity_type == EntityType.CONTACT:
            # Name matches are most relevant
            if query in entity.name.value.lower():
                score += 2.0
            
            # Exact name match is even better
            if entity.name.value.lower() == query:
                score += 1.0
            
            # Other field matches
            if (entity.phone and query in entity.phone.value.lower()):
                score += 0.5
            if (entity.email and query in entity.email.value.lower()):
                score += 0.5
            if (entity.address and query in entity.address.value.lower()):
                score += 0.3

        elif entity_type == EntityType.NOTE:
            # Text contains query
            if query in entity.text.lower():
                score += 1.0
            
            # Multiple occurrences increase relevance
            occurrences = entity.text.lower().count(query)
            score += occurrences * 0.2
            
            # Tag matches
            if any(query in tag.lower() for tag in entity.tags):
                score += 1.5

        return score

    def get_entity_by_hit(self, search_hit: SearchHit) -> Any:
        if search_hit.entity_type == EntityType.CONTACT:
            return self.contacts.get_by_id(search_hit.entity_id)
        elif search_hit.entity_type == EntityType.NOTE:
            return self.notes.find(search_hit.entity_id)
        
        return None
