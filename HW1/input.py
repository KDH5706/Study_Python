import RPi.GPIO as GPIO
import time

switchPin = 11
ledPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

led_state = True

try:
    while True :
        if GPIO.input(switchPin) == 1:
            GPIO.output(ledPin, led_state)
            led_state = 1 - led_state
            time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()

    
