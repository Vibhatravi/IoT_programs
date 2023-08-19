import time
import RPi.GPIO as GPIO

touchpin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(touchpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def touch_det(pin):
	touch = GPIO.input(pin)
	return touch
try:
	while True:
		if touch_det(touchpin):print('['+time.ctime()+']-'+'Touch Detected')
		time.sleep(0.2)
except KeyboardInterrupt:
	print('Keyboard interupted')
	GPIO.cleanup()
