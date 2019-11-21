class Catalog(object):

    def __init__(self):
        self._book = []

    def description(self):
        return """\
# Alexandra's Catalog

{}
""".format(
            self._book[0].description() if self._book
            else "No books available at the moment"
        )

    def book(self):
        return None if not self._book else self._book[0]

    def addBook(self, book):
        self._book.append(book)
