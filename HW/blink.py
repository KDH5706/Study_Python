import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
#GPIO.setup(21, GPIO.OUT)

while True :
    GPIO.output(18, True)
    #GPIO.output(21, True)
    time.sleep(1)
    
    GPIO.output(18, False)
    #GPIO.output(21, False)
    time.sleep(1)
    