import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 15
from gpiozero import Button
def button_pressed():
	print("Button pressed")
def button_released():
	print("Button released")

button = Button(23)
button.when_pressed = button_pressed
button.when_released = button_released

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature,humidity))
