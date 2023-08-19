import serial
import time

ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.reset_input_buffer()
time.sleep(3)

try:
	while True:
		ser.write(b"Hello this is raspberry\n")
		line=ser.readline().decode('utf-8').rstrip()
		print(line)
		time.sleep(2)
except KeyboardInterrupt:
	print("Keyboard Interrupted")
	ser.close()
