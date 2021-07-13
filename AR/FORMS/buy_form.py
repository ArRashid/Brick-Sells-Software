from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QDialog,QFileDialog
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import  QTimer
import cv2

import shutil # for copy file


################ My madulse ###########

from AR.DATABASE import *

#######################################

class BuyForm(QDialog):
    def __init__(self):
        file = os.path.join("AR","FORMS","buy_form.ui")
        super(BuyForm, self).__init__()
        loadUi(file, self)

        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.camera.clicked.connect(self.controlTimer)
        self.pic_path = None #for saving Uploaded Image pathc
        self.browse.clicked.connect(self.Browse)
        self.upload = None # browse file pah refarence
        self.capture = None # refare to the camear captre photo in temp folder

        self.save.clicked.connect(self.Save)


    def Browse(self):
        self.upload = QFileDialog.getOpenFileName(self, 'Open a file', '','Picture Only (*.png *.jpg *.jepg *.bmp )')
        self.pic.setPixmap(QPixmap(self.upload[0]))


    def Save(self):
        print("worked upto save ")

        #upload image from browse button
        try:
            if self.upload != None and not self.timer.isActive():
                print("in if mode")
                print(self.upload)
                filename = "Data/Upload/ChallanScan/Challan_Scan_Copy_of_" + self.field.text() + "_date_" + self.date.text() + "challan no : "+ self.challan.text() +"at AR .jpg"
                dest = os.path.join(os.getcwd(), filename)
                shutil.copyfile(self.upload[0], dest)
                self.pic_path = filename


            elif not self.timer.isActive() and self.upload == None:
                filename = "Data/Upload/ChallanScan/Challan_Scan_Copy_of_" + self.field.text() + "_date_" + self.date.text() + "challan no : "+ self.challan.text() +"at AR .jpg"
                dest = os.path.join(os.getcwd(), filename)
                shutil.copyfile(self.capture, dest)
                self.pic_path = filename
            else:
                filename = "empty challan"
                self.pic_path = filename


        except:
            filename = "empty challan"
            self.pic_path = filename



        print("hare")
        #save data to database by this lines
        save = SqLite("data.db")
        save.Add('''
        INSERT INTO BuyVouchar
        VALUES ('{0}', '{1}', '{2}','{3}' , '{4}', '{5}','{6}')
        
        '''.format(562,"none","no date","field adarsha","wb32 d3242","23","data base test"))

        print(self.pic_path)
        print("all ok")

            # self.bid.text(),
            #                self.pic_path, 33
            #                self.date.text(),
            #                self.field.currentText(),
            #                self.carno.text(),
            #                self.challan.text(),
            #                self.note.text()
            #                ))






        # after save Reset Field by this lines



    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, self.frems = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(self.frems, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.pic.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer an capture frome camera
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.camera.setText("Capture")
        # if timer is started
        else:
            dest = os.path.join(os.getcwd(),".Temp", "temp.jpg") #temporary path for captured photos
            cv2.imwrite(dest, self.frems) # image save mthod
            self.capture = dest #temporary address asing to global
            self.upload = None # clear if any Browse file is there
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.camera.setText("Re-Connect")
            print("re cap")

# a = SqLite("data.db")
#
#
# a.Add('''CREATE TABLE Accounts (
#     name text,
#     address text,
#     phone text,
#     email text,
#     type text,
#     bal integer,
#     pf text
# )''')