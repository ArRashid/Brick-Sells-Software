from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QDialog,QFileDialog,QPushButton,QComboBox,QTableWidgetItem
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import  QTimer,QDate
import cv2

import shutil # for copy file

from datetime import date



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


        #form Int value 
        db = SqLite("data.db")
        self.b_id.setText(str(len(db.View("SELECT * FROM BuyVouchar"))+1))
        db.Close()
        self.today = date.today()
        self.date.setDate(QDate(self.today))
        self.field.setCurrentText("select")


        self.addbtn = QPushButton("add")
        
        self.addbtn.clicked.connect(self.add_row)
        self.pdlist = ["No 1 Picket","No 2 Brick","No 3 Picket","No 4 Bricks","No 5 Picket","Base"]
        self.combo = QComboBox()
        self.combo.addItems(self.pdlist)
        
        
        


        
        self.get_itemvalue = []
        self.add_row()



    def Browse(self):
        self.upload = QFileDialog.getOpenFileName(self, 'Open a file', '','Picture Only (*.png *.jpg *.jepg *.bmp )')
        self.pic.setPixmap(QPixmap(self.upload[0]))


    def Save(self):
        self.save = SqLite("data.db")
        #upload image from browse button
        try:
            if self.upload != None and not self.timer.isActive():
                print("in if mode")
                print(self.upload)
                filename = "Data/Upload/ChallanScan/Challan_Scan_Copy_of_" + self.field.currentText() + "_date_" + str(self.date.date()) + "_challan_"+ str(self.challan.text()) +"_at_AR.jpg"
                dest = os.path.join(os.getcwd(), filename)
                shutil.copyfile(self.upload[0], dest)
                self.pic_path = filename
                print(filename)
            elif not self.timer.isActive() and self.upload == None:
                filename = "Data/Upload/ChallanScan/Challan_Scan_Copy_of_" + self.field.currentText() + "_date_" + str(self.date.date()) + "_challan_"+ str(self.challan.text()) +"_at_AR.jpg"
                dest = os.path.join(os.getcwd(), filename)
                shutil.copyfile(self.capture, dest)
                self.pic_path = filename
            else:
                filename = "empty challan"
                self.pic_path = filename
        except:
            filename = "empty challan"
            self.pic_path = filename


        #save data to database by this lines
        
        self.save.Add('''
        INSERT INTO BuyVouchar
        VALUES ('{0}', '{1}', '{2}','{3}' , '{4}', '{5}','{6}')
        
        '''.format(self.b_id.text(),self.pic_path,self.date.date(),self.field.currentText(),self.carno.text(),self.challan.text(),self.note.toPlainText()))
        self.tabledata()
        self.tableeras()
        

        # Reset Form
        self.b_id.setText(str(len(self.save.View("SELECT * FROM BuyVouchar"))+1))
        self.pic_path = None
        self.date.setDate(QDate(self.today))
        self.field.setCurrentText("select")
        self.carno.setText("")
        self.challan.setText("")
        self.note.setPlainText("")
        self.pic.setText("")
        

        print(self.pic_path)
        print("all ok")
        
        print("tabl also called")

    def tabledata(self):
        # print(self.table.item(0, 0).text())

        rows = self.table.rowCount()
        
        
        for row in range(rows):
            print("rows :",rows,"row ;",row)
            id = len(self.save.View("SELECT * FROM BuyProduct"))+1
            try:
                    quantity = int(self.table.item(row, 1).text())
            except:
                quantity = 0

            try:
                rate = int(self.table.item(row, 2).text())
            except:
                rate = 0
            try:
                remark = int(self.table.item(row, 3).text())
            except:
                remark = ""
            
            
            if row == rows -1:
                

                self.save.Add('''
                INSERT INTO BuyProduct
                VALUES ({0}, '{1}', {2}, {3}, '{4}',{5})
                '''.format(
                id,
                self.combo.currentText(),
                quantity,
                rate,
                remark,
                self.b_id.text()
                ))
                
            else:
                print("in else")
                print(rows)
                self.save.Add('''
                INSERT INTO BuyProduct
                VALUES ({0}, '{1}', {2}, {3}, '{4}',{5})
                '''.format(
                id,
                self.table.item(row, 0).text(),
                quantity,
                rate,
                remark,
                self.b_id.text()
                ))
            
            
    
        

   

        

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


    def tableeras(self):
        rows =  self.table.rowCount()+1
        for row in range(rows):
            print("SSSSSSSSSSSSSSSS",row,"of",rows)
        self.table.setRowCount(1)
            # self.table.removeRow((rows -row)-1)
        
        


    def add_row(self):
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        
        self.table.setCellWidget(self.table.rowCount()-1,4,self.addbtn)
        self.table.setCellWidget(self.table.rowCount()-1,0,self.combo)     
        
        self.table.setItem(row -1,0,QTableWidgetItem(self.combo.currentText()))
         


    
        

    print("all ok")