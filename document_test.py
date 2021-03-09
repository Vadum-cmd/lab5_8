from document import Document
from character import Character


def main():
    # Creating new Document.
    doc = Document()

    # Adding new character.
    doc.insert(Character("a", True, True))
    print(doc.string)

    # Adding new character.
    doc.insert(Character("b", True, False, False))
    print(doc.string)

    # Deleting last character.
    doc.delete()

    # Saving changes.
    doc.save()
    print(doc.string)

    # Adding new character.
    doc.insert(Character("c", True, False, True))
    print(doc.string)

    # Adding new character.
    doc.insert(Character("d", False, True, True))
    print(doc.string)

    # Deleting character where cursor is located.
    doc.cursor.back()
    doc.delete()
    print(doc.string)

    # --------------------------------------------
    # a.i) Moving cursor to the start and further.
    # --------------------------------------------
    # doc.cursor.home()
    # doc.cursor.back()
    # --------------------------------------------
    # Nothing happens.
    # --------------------------------------------
    # a.ii) Moving cursor after end of the file.
    # --------------------------------------------
    # doc.cursor.end()
    # doc.cursor.forward()
    # --------------------------------------------
    # Nothing happens.
    # --------------------------------------------
    # b) Deleting character which doesn't exist.
    # --------------------------------------------
    # doc.cursor.home()
    # doc.delete()
    # print(doc.string)
    # --------------------------------------------
    # Last character is deleted.
    # --------------------------------------------
    # c) Saving file without a name.
    # --------------------------------------------
    # Error raises(you simply cannot).
    # --------------------------------------------
    # d) Entering several characters at once.
    # --------------------------------------------
    # Error raises(you can add only one character at time).
    # --------------------------------------------

    # Saving changes.
    doc.save()


if __name__ == "__main__":
    main()
