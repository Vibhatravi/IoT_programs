import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servopin = 18
touchpin = 23

GPIO.setup(servopin,GPIO.OUT)
servo = GPIO.PWM(servopin,50)
servo.start(0)

GPIO.setup(touchpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def move_servo(angle):
	duty_cycle = 2 + (angle/18)
	servo.ChangeDutyCycle(duty_cycle)
	time.sleep(0.3)

def touch_callback(channel):
	print("Touch sensor pressed")
	move_servo(5)

GPIO.add_event_detect(touchpin,GPIO.FALLING,callback=touch_callback,bouncetime=200)
try:
	while True:
		time.sleep(0.1)
except KeyboardInterrupt:
	servo.stop()
	GPIO.cleanup()
