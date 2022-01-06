import unittest
from src.notes_service import NotesService
from src.note import Note
from unittest.mock import MagicMock, patch


class Test_NotesService(unittest.TestCase):
    def setUp(self):
        self.notes_service = NotesService()

    @patch("src.NotesStorage.add")
    def test_add_positive(self, mock_add: MagicMock):
        note = Note("test", 3.0)
        mock_add.return_value = note
        added_note = self.notes_service.add(note)
        self.assertEqual(added_note, note)

    @patch("src.NotesStorage.getAllNotesOf")
    def test_averageOf(self, mock_getAllNotesOf: MagicMock):
        mock_getAllNotesOf.return_value = [Note("test1", 3.5), Note("test1", 2.0), Note("test1", 4.5)]
        self.assertEqual(self.notes_service.averageOf("test1"), 3.33)

    @patch("src.NotesStorage.getAllNotesOf")
    def test_averageOf_None(self, mock_getAllNotesOf: MagicMock):
        mock_getAllNotesOf.return_value = []
        self.assertIsNone(self.notes_service.averageOf("test"))

    @patch("src.NotesStorage.clear")
    def test_clear(self, mock_clear: MagicMock):
        mock_clear.return_value = None
        self.assertIsNone(self.notes_service.clear())
