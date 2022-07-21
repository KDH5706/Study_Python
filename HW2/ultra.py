import RPi.GPIO as GPIO
import time

triggerPin = 20
echoPin = 21

def measure():
    GPIO.output(triggerPin, True)
    time.sleep(0.000010)
    GPIO.output(triggerPin, False)
    start = time.time()
    
    while GPIO.input(echoPin) == False :
        start = time.time()
    while GPIO.input(echoPin) == True :
        stop = time.time()
        
    check_time = stop - start
    distance = (check_time * 34300) / 2
    
    return distance
    

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

GPIO.output(triggerPin, False)


try:
    while True:
        distance = measure()
        print("Distamce : %.2f cm" %distance)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    
GPIO.cleanup()


