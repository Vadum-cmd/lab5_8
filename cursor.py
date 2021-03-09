class Cursor:
    def __init__(self, document):
        """
        Initializing cursor.
        """
        self.document = document
        self.position = 0


    def forward(self):
        """
        Moving forward by one.
        """
        self.position += 1


    def back(self):
        """
        Moving back by one.
        """
        self.position -= 1


    def home(self):
        """
        Moving to start of the document.
        """
        while (self.position - 1) != 0:
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break


    def end(self):
        """
        Moving to end of the document.
        """
        while self.position < len(self.document.characters) and  self.document.characters[self.position] != '\n':
            self.position += 1
