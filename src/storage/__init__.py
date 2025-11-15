"""
Handles persistent data storage (read/write to disk).

Re-export FileStore for convenient imports:

    from src.storage import FileStore
"""

from .file_store import FileStore

__all__ = ["FileStore"]
