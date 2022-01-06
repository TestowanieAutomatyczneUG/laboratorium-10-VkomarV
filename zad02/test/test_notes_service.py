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
