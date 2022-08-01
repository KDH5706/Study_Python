import sys
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
from PyQt5 import uic
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT = 26
LED = 19
TRIG = 20
ECHO = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED,GPIO.OUT)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)

form_class = uic.loadUiType("raspi.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnDIST.clicked.connect(self.DISTANCE_btn_clicked)
        self.btnON.clicked.connect(self.LED_ON_btn_clicked)
        self.btnOFF.clicked.connect(self.LED_OFF_btn_clicked)
        self.btnTH.clicked.connect(self.TeHu_btn_clicked)

    def DISTANCE_btn_clicked(self):
        GPIO.output(TRIG,True)
        time.sleep(0.000010)
        GPIO.output(TRIG,False)
        
        while GPIO.input(ECHO) == 0:
            start = time.time()
            
        while GPIO.input(ECHO) == 1:
            stop = time.time()
            
        check_time = stop-start
        distance = (check_time * 34300) / 2
        
        self.lblDis.setText("Distance : %.1f cm" % distance)
        
    def LED_ON_btn_clicked(self):
        GPIO.output(LED, True)
        
    def LED_OFF_btn_clicked(self):
        GPIO.output(LED, False)
        
    def TeHu_btn_clicked(self):
        h, t = Adafruit_DHT.read_retry(sensor, DHT)

        if h is not None and t is not None :
            self.lblHu.setText("Humid : %.1f" % h)
            self.lblTe.setText("Temp : %.1f" % t)
        else :
            self.lblHu.setText("Humid : 0")
            self.lblTe.setText("Temp : 0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowClass()
    window.show()
    app.exec_()
    