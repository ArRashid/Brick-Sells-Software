import sqlite3
import os


class SqLite():
    def __init__(self, database):
        path = os.path.join(os.path.dirname(os.path.join(os.getcwd(), os.pardir)),'Data',database)
        self.conn = sqlite3.connect(path)
        self.cour = self.conn.cursor()

    def Add(self, quarry):
        self.cour.execute(quarry)
        self.conn.commit()




    def View(self, quarry):
        self.cour.execute(quarry)
        try:
            if len(self.cour.fetchall()) > 1:
                return self.cour.fetchall()
            else:
                return self.cour.fetchone()
        finally:
            self.conn.commit()


