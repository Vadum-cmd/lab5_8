from cursor import Cursor
from character import Character


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = 'plain_text.txt'


    def insert(self, character: Character):
        self.characters.insert(self.cursor.position, character)
        self.cursor.end()


    def delete(self):
        del self.characters[self.cursor.position - 1]


    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()


    @property
    def string(self):
        return "".join(self.characters)
