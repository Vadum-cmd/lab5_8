from cursor import Cursor
from character import Character


class Document:
    def __init__(self):
        """
        Initializing new Document.
        """
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = 'plain_text.txt'


    def insert(self, character: Character):
        """
        Inserting new character in the document.
        """
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()


    def delete(self):
        """
        Deleting previous character according to cursor.
        """
        del self.characters[self.cursor.position - 1]


    def save(self):
        """
        Saving changes to your document.
        """
        f = open(self.filename, 'w')
        f.write(self.string)
        f.close()


    @property
    def string(self):
        """
        Converting list of Characters to string.
        """
        return "".join(str(character) for character in self.characters)
