class Book(object):

    def __init__(self):
        self._title = "untitled"

    def title(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def isOnSale(self):
        return False
