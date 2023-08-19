import RPi.GPIO as GPIO
import time
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 15
while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature,humidity))
