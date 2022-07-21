import RPi.GPIO as GPIO
import time

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

triggerPin = 20
echoPin = 21
piezoPin = 13
    

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)


GPIO.output(triggerPin, False)
Buzz = GPIO.PWM(piezoPin, 440)

state = True

try:
    while True:
        buz_delay = 0
        distance = measure()
        print("Distamce : %.2f cm" %distance)

        if distance < 5 :
            buz_delay = 0.2
        elif 5 <= distance < 7 :
            buz_delay = 0.3
        elif 7 <= distance < 9 :
            buz_delay = 0.4
        elif 9 <= distance < 11 :
            buz_delay = 0.5
        elif 11 <= distance < 13 :
            buz_delay = 0.6
        else:
            time.sleep(0.5)
            continue
        
        if state == True :
            Buzz.start(50)
            Buzz.ChangeFrequency(110)
            time.sleep(buz_delay)
            Buzz.stop()
        else :
            time.sleep(buz_delay)
            
        state = 1 - state

except KeyboardInterrupt:
    GPIO.cleanup()
    
GPIO.cleanup()



