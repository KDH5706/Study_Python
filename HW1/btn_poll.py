import RPi.GPIO as GPIO
import time

On_Pin = 11
Off_Pin = 6
ledPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(On_Pin, GPIO.IN)
GPIO.setup(Off_Pin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

led_state = True
count = 0
try:
    while True :
        if GPIO.input(On_Pin) == 1:
            GPIO.output(ledPin, False)
        if GPIO.input(Off_Pin) == 1:
            GPIO.output(ledPin, True)

except KeyboardInterrupt:
    GPIO.cleanup()

    

