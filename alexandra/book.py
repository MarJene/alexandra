class Book(object):

    def __init__(self):
        self._title = "untitled"
        self._onSale = False
        self._author = "Anonymous"

    def title(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def isOnSale(self):
        return self._onSale

    def putOnSale(self):
        self._onSale = True

    def author(self):
        return self._author

    def setAuthor(self, author):
        self._author = author
