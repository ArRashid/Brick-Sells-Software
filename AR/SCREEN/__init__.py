from PyQt5 import QtWidgets

class MainScreen():

    def __init__(self):
        self.widget = QtWidgets.QStackedWidget()
        self.widget.setMinimumHeight(600)
        self.widget.setMinimumWidth(800)
        self.widget.setWindowTitle = "Project name"
        self.widget.show()
        print("in Main inti",self.widget.currentWidget())




    def addwin(self,windos):
        # add windows
        self.widget.addWidget(windos)
    def hide(self):
        # destory windows
        self.widget.hide()

    def goto(self,index):
        #by this option you can changw windows using index no
        self.widget.setCurrentIndex(index)

    def froward(self):
        #forward windos from current windows
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def backward(self):
        #backward windwos form current windows
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
