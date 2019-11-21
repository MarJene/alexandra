class Catalog(object):

    def __init__(self):
        self._book = None

    def description(self):
        return """\
# Alexandra's Catalog

{}
""".format(
            self._book.description() if self._book
            else "No books available at the moment"
        )

    def book(self):
        return self._book

    def addBook(self, book):
        self._book = book
