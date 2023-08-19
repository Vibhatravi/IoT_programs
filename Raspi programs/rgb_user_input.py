import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
led_choice = 0
count = 0

os.system('clear')

print("Which LED you Want to blink?")
print("1:RED")
print("2:GREEN")
print("3:BLUE")
print("4:ALL")
led_choice = int(input("Make your choice: "))

if led_choice == 1:
	os.system('clear')
	print("You choose red led")
	count = int(input("How many times you want it blink?: "))
	while count > 0:
		GPIO.output(29,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(29,GPIO.LOW)
		time.sleep(0.2)
		count = count - 1
elif led_choice == 2:
	os.system('clear')
	print("You choose green led")
	count = int(input("How many times you want it blink?: "))
	while count > 0:
		GPIO.output(31,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(31,GPIO.LOW)
		time.sleep(1)
		count = count - 1
elif led_choice == 3:
        os.system('clear')
        print("You choose blue led")
        count = int(input("How many times you want it blink?: "))
        while count > 0:
                GPIO.output(33,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(33,GPIO.LOW)
                time.sleep(1)
                count = count - 1
elif led_choice == 4:
	os.system('clear')
	print("You choose all led's")
	count = int(input("How many times you want it blink?: "))
	while count > 0:
		GPIO.output(29,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(29,GPIO.LOW)
		time.sleep(1)
		GPIO.output(31,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(31,GPIO.LOW)
		time.sleep(1)
		GPIO.output(33,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(33,GPIO.LOW)
		time.sleep(1)
		count = count - 1
GPIO.cleanup()
