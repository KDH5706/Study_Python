from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello!'

@app.route('/Led/<string:led_state>')
def Led(led_state):
	if led_state == 'on' :
		GPIO.output(12, True)
		return 'LED : ON!'

	if led_state == 'off':
		GPIO.output(12, False)
		return 'LED : OFF!'

	return 'Hello!~'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
