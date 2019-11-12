import sqlite3

class Rekordkeeper(object):

    def __init__(filename="log"):
        self.file = filename + ".sqlite"
        self.db = sqlite3.connect(self.file)
        self.c = self.db.cursor()
