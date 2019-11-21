class Catalog(object):

    def __init__(self):
        self._books = []

    def description(self):
        return """\
# Alexandra's Catalog

{}
""".format(
        "No books available at the moment" if not self._books
        else self.listBooks()
    )

    def books(self):
        return None if not self._books else self._books[0]

    def addBook(self, book):
        self._books.append(book)

    def listBooks(self):
        items = ""
        for book in self._books:
            items = items + "- {}\n".format(book.description())
        return items
