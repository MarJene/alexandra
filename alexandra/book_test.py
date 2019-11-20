import unittest
from .book import Book


class Book_Test(unittest.TestCase):

    def test_title_byDefault(self):
        book = Book()
        self.assertEqual(book.title(), "untitled")

    def test_title_whenSet(self):
        book = Book()
        book.setTitle("Harry Potter 1")
        self.assertEqual(book.title(), "Harry Potter 1")

    def test_isOnSale_byDefault(self):
        book = Book()
        self.assertFalse(book.isOnSale())

    def _test_isOnSale_whenSet(self):
        book = Book()
        book.putOnSale()
        self.assertEqual(book.isOnSale(), True)