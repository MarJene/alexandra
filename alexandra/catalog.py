class Catalog(object):

    def __init__(self):
        self._book = []

    def description(self):
        return """\
# Alexandra's Catalog

{}
""".format(
        "No books available at the moment" if not self._book
        else self._listBooks()
    )

    def book(self):
        return None if not self._book else self._book[0]

    def addBook(self, book):
        self._book.append(book)

    def _listBooks(self):
        items = ""
        for book in self._book:
            items = items + "- {}\n".format(book.description())
        return items
