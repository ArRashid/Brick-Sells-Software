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
            record = self.cour.fetchall()
            print("in try ")
            if len(record) > 1:
                print("in try if")
                return record
            else:
                print("in try els")
                return self.cour.fetchone()
        except:
            print("in exxx")
            return self.cour.fetchall()
        finally:
            self.conn.commit()
    def Close(self):
        self.conn.close()


