import sys
# import cv2
# from PyQt5 import QtCore,QtGui,QtMultimedia
from PyQt5.uic import loadUi
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget, QWidget

# from PyQt5.QtGui import QPixmap, QColor #camera
# from PyQt5.QtGui import QImage,QPixmap
# from PyQt5.QtCore import QTimer,QDateTime


# ################## my own maduls ##################
from AR.FORMS.addaccount import AddAccountForm
from AR.FORMS.buy_form import BuyForm
from AR.SCREEN import MainScreen

#####################################################

class mainwin(QMainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        loadUi('main.ui', self)
        #Docked Windows Buttons 
        self.bt_account.clicked.connect(self.Bt_account)
        self.bt_buying.clicked.connect(self.Bt_buying)
        self.bt_selling.clicked.connect(self.Bt_selling)
        self.bt_stock.clicked.connect(self.Bt_stock)
        self.bt_others.clicked.connect(self.Bt_others)
        self.bt_reporting.clicked.connect(self.Bt_reporting)
        #Main Bar Icons or Buttons
        self.bt_addaccount.clicked.connect(self.Add_account)
        self.bt_buyvouchar.clicked.connect(self.Buy_Vou)



        


    def Bt_account(self):
        pass
    def Bt_buying(self):
        print("buying")
    def Bt_selling(self):
        print("selling ")
    def Bt_stock(self):
        print('stock')
    def Bt_others(self):
        print("others")
    def Bt_reporting(self):
        print("reporting ")

    

    def Add_account(self):
        win.goto(2)

    def Buy_Vou(self):
        win.goto(3)




class add_ac_form(AddAccountForm):
    def __init__(self):
        super().__init__()
        self.exit.clicked.connect(self.Exit)
    def Exit(self):
        win.goto(1)

class Buy_Form(BuyForm):
    def __init__(self):
        super().__init__()
        self.exit.clicked.connect(self.Exit)
    def Exit(self):
        win.goto(1)



class loginwin(QDialog):
    def __init__(self):
        super(loginwin, self).__init__()
        loadUi('login.ui', self)
        self.login.clicked.connect(self.Login)

    def Login(self):
        user = self.username.text()
        password = self.password.text()

        if len(user) <= 0 or len(password) <= 0:
            self.error.setText("Plase Fillup All Field !")
        else:
            if user == "ar" and password == "123":
                print("login success", user, password)
                win.froward()
            else:
                self.error.setText("Username or Password isn't Match ! ")





def Run():
    global win
    app = QApplication(sys.argv)
    win = MainScreen()
    win.addwin(loginwin())
    win.addwin(mainwin())     # No 1
    win.addwin(add_ac_form()) # no 2
    win.addwin(Buy_Form())    # no 3




    print("Run Is RuNNED")

    try:
        sys.exit(app.exec())
    except:
        print("Exiting")





if __name__ == "__main__":
    Run()






