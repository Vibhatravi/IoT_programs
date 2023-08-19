import serial
import time

if __name__=='__main__':
	ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
	time.sleep(3)
	ser.reset_input_buffer()
	
	try:
		while True:
			if ser.in_waiting>0:
				line=ser.readline().decode('utf-8').rstrip()
				#line=ser.readline().rstrip()
				print(line)
				time.sleep(0.01)
	except KeyboardInterrupt:
		print("Keyboard Interrupted")
		ser.close()
