import unittest
from .catalog import Catalog
from somutils import testutils
from .book import Book


class Catalog_Test(unittest.TestCase):

    def test_description_empty(self):
        catalog = Catalog()
        description = catalog.description()
        self.assertEquals(description, """\
# Alexandra's Catalog

No books available at the moment
""")

    def test_description_oneBook(self):
        catalog = Catalog()
        book = Book()
        catalog.addBook(book)
        self.assertEqual(catalog.description(), """\
# Alexandra's Catalog

- {}

""".format(book.description()))

    def test_book_byDefault(self):
        catalog = Catalog()
        self.assertEqual(catalog.book(), None)

    def test_book_whenSet(self):
        catalog = Catalog()
        book = Book()
        catalog.addBook(book)
        self.assertEqual(catalog.book(), book)

    def _test_description_manyBooks(self):
            catalog = Catalog()
            book1 = Book()
            book2 = Book()
            catalog.addBook(book1)
            catalog.addBook(book2)
            self.assertEqual(catalog.description(), """\
# Alexandra's Catalog

- {}
- {}

""".format(book1.description(), book2.description()))

    def test_listBooks_byDefault(self):
        catalog = Catalog()
        self.assertEqual(catalog._listBooks(), "No books available at the moment")