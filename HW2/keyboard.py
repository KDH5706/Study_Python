import RPi.GPIO as GPIO
import time

piezoPin = 13

melody = [262, 294, 330, 349, 392, 440, 494, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
    while True:
        try:
            num = int(input('press keyboard (0 ~ 7) : '))
            if 0 <= num <= 7 :
                pass
            else :
                print("Out of range value")
                continue
            Buzz.start(50)
            Buzz.ChangeFrequency(melody[num])
            time.sleep(0.5)
            Buzz.stop()
            
        except ValueError:
            print("long value")

except KeyboardInterrupt:
    GPIO.cleanup()
    
GPIO.cleanup()

