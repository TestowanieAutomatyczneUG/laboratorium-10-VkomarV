import unittest
from assertpy import assert_that
from src.note import Note

class NoteTest(unittest.TestCase):
    def test_get_name(self):
        note = Note()
        assert_that(note.get_name()).is_equal_to("note")

    def test_get_note(self):
        note = Note()
        assert_that(note.get_note()).is_equal_to(4.4)

    def test_get_note_min(self):
        note = Note("note", 2.0)
        assert_that(note.get_note()).is_equal_to(2.0)

    def test_get_Note_max(self):
        note = Note("spr", 6.0)
        assert_that(note.get_note()).is_equal_to(6.0)
    def test_get_name_empty(self):
        self.assertRaises(Exception, Note, "")

    def test_get_name_tab(self):
        self.assertRaises(Exception, Note, [])

    def test_get_name_none(self):
        self.assertRaises(Exception, Note, None)

    def test_get_note_too_low(self):
        self.assertRaises(Exception, Note, "test", 1.0)

    def test_get_note_too_high(self):
        self.assertRaises(Exception, Note, "test", 7.0)

    def test_get_note_nuno(self):
        self.assertRaises(Exception, Note, "test", None)
