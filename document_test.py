from document import Document
from character import Character


def main():
    # Creating new Document.
    doc = Document()

    # Adding new character.
    doc.insert(str(Character("a", True, True)))
    print(doc.string)

    # Adding new character.
    doc.insert(str(Character("b", True, False, False)))
    print(doc.string)

    # Deleting last character.
    doc.delete()
    doc.save()
    print(doc.string)

    # Adding new character.
    doc.insert(str(Character("c", True, False, True)))
    print(doc.string)

    # Adding new character.
    doc.insert(str(Character("d", False, True, True)))
    print(doc.string)

    # Deleting character where cursor is located.
    doc.cursor.back()
    doc.delete()
    print(doc.string)
    # Saving changes.
    doc.save()


if __name__ == "__main__":
    main()
