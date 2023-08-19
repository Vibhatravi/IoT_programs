import RPi.GPIO as GPIO
import time
redpin = 40
bluepin = 38
greenpin = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redpin,GPIO.OUT)
GPIO.setup(bluepin,GPIO.OUT)
GPIO.setup(greenpin,GPIO.OUT)
while(True):
	ch=input("enter the color: ")
	if(ch=="red"):
		GPIO.output(redpin,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(redpin,GPIO.LOW)
		time.sleep(1)
	elif(ch=="green"):
		GPIO.output(greenpin,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(greenpin,GPIO.LOW)
		time.sleep(1)
	elif(ch=="blue"):
		GPIO.output(bluepin,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(bluepin,GPIO.LOW)
		time.sleep(1)
	elif(ch=="rgb"):
		GPIO.output(redpin,GPIO.HIGH)
		GPIO.output(greenpin,GPIO.HIGH)
		GPIO.output(bluepin,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(redpin,GPIO.LOW)
		GPIO.output(greenpin,GPIO.LOW)
		GPIO.output(bluepin,GPIO.LOW)
	elif(ch=="rg" or ch=="gr"):
		GPIO.output(redpin,GPIO.HIGH)
		GPIO.output(greenpin,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(redpin,GPIO.LOW)
		GPIO.output(greenpin,GPIO.LOW)
	elif(ch=="rb" or ch=="br"):
		GPIO.output(redpin,GPIO.HIGH)
		GPIO.output(bluepin,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(redpin,GPIO.LOW)
		GPIO.output(bluepin,GPIO.LOW)
	elif(ch=="gb" or ch=="bg"):
		GPIO.output(bluepin,GPIO.HIGH)
		GPIO.output(greenpin,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(bluepin,GPIO.LOW)
		GPIO.output(greenpin,GPIO.LOW)
	else:
		break
