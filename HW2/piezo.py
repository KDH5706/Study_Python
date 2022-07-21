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
        Buzz.start(50)
        for i in range(0, len(melody)):
            Buzz.ChangeFrequency(melody[i])
            time.sleep(0.3)
        Buzz.stop()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
