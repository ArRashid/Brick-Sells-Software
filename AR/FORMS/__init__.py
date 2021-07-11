import cv2
import os
import shutil # for copy file
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QImage

class SaveImage(object):
    def __init__(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)




    def BrowseCopy(self,Copy_Source,Copy_destination):
    	shutil.copyfile(Copy_Source,Copy_destination)
        

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
        return qImg

    # start/stop timer an capture frome camera
    def Capture(self,Capture_Path):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text

        # if timer is started
        else:
            cv2.imwrite(Capture_Path, self.frems) # image save mthod
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()


