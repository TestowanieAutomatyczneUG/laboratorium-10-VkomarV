class Note:

    def __init__(self, name="note", note=4.4):
        if type(name) is not str or name == "":
            raise Exception("Wrong type val")
        else:
            self.name = name

        if type(note) is float:
            if 2.0 <= note <= 6.0:
                self.note = note
            else:
                raise ValueError()
        else:
            raise TypeError()

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
