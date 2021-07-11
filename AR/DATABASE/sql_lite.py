import sqlite3

class SqLite():
    def __init__(self,database):
        self.conn = sqlite3.connect(database)
        self.cour = self.conn.cursor()

    def Add(self,quarry):
        self.cour.execute(quarry)
        self.conn.commit()

    def View(self,quarry):
        self.cour.execute(quarry)
        try:
            if len(self.cour.fetchall()) > 1 :
                return self.cour.fetchall()
            else:
             return self.cour.fetchone()
        finally:
            self.conn.commit()





