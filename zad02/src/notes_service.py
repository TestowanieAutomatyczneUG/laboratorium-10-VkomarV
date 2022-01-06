from src.note import Note
from src.notes_storage import NotesStorage


class NotesService:
    def __init__(self):
        self.notesStorage = NotesStorage()

    def add(self, note: Note):
        return self.notesStorage.add(note)

    def averageOf(self, name: str):
        notes = self.notesStorage.getAllNotesOf(name)
        if len(notes) == 0:
            return None
        notes_sum = 0
        for note in notes:
            notes_sum += note.note
        return round(notes_sum / len(notes), 2)

    def clear(self):
        return self.notesStorage.clear()
