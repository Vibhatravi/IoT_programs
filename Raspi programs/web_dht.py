import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

host_name = '192.168.63.237'  # Change this to your Raspberry Pi IP address
host_port = 8000


class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """

        html = '''
           <html>
           <head>
            <meta http-equiv="refresh" content="2">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script></head>
           <body>
           <div class="display-1 text-center">Welcome to my Raspberry Pi</div><br><br>
           <div class="container">
           <div class="row">
           <div class="col-sm-4">
           <div class="card"><div class="card-title display-3">LED</div><div class="card-body"><p>Current GPU temperature is {}</p><br>
            <div class="progress">
                <div class="progress-bar" style="width:{}%">{}</div>
            </div><br><br>
           <p>Turn LED: <button class="btn btn-success"><a style="text-decoration:None" class=" text-white" href="/on">On</a></button> <button class="btn btn-danger"><a style="text-decoration:None" class=" text-white" href="/off">Off</a></button></p></div><br>
           <div class="card-footer"><div id="led-status"></div></div></div></div>

           <div class="col-sm-4">
           <div class="card"><div class="card-title display-3">ULTRASONIC</div><div class="card-body">The Distance is : {} cm <br>
            <div class="progress">
                <div class="progress-bar bg-danger" style="width:{}%">{}</div>
            </div><br><br></div>
            &nbsp;&nbsp;<p>Turn ULTRASONIC: <button class="btn btn-primary"><a style="text-decoration:None" class=" text-white" href="/read">Read</a></button></p><div><div id="ultra"></div><br>
           <div class="card"><div class="card-title display-3">ULTRASONIC</div><div class="card-body">The Distance is : {} cm <br>
           <div class="card"><div class="card-title display-3">ULTRASONIC</div><div class="card-body">The Distance is : {} cm <br>
          </div></div>
           </div></div></div>
           <script>
                document.getElementById("ultra").innerHTML="{}";
                document.getElementById("led-status").innerHTML="{}";
           </script>
           </body>
           </html>
        '''
        temp = os.popen("vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        distance=0;
        GPIO_TRIGGER = 23
        GPIO_ECHO = 24
        sensor = Adafruit_DHT.DHT11
        pin = 15
        if self.path=='/':
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18, GPIO.OUT)
 
             #set GPIO direction (IN / OUT)
            GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
            GPIO.setup(GPIO_ECHO, GPIO.IN)

        elif self.path=='/on':
            GPIO.output(18, GPIO.HIGH)
            status='LED is On'
        elif self.path=='/off':
            GPIO.output(18, GPIO.LOW)
            status='LED is Off'
        elif self.path=='/read':
            #distance calculation
            # set Trigger to HIGH
            GPIO.output(GPIO_TRIGGER, True)
 
            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER, False)
 
            StartTime = time.time()
            StopTime = time.time()
 
            # save StartTime
            while GPIO.input(GPIO_ECHO) == 0:
                StartTime = time.time()
 
                # save time of arrival
                while GPIO.input(GPIO_ECHO) == 1:
                    StopTime = time.time()
 
                    # time difference between start and arrival
                    TimeElapsed = StopTime - StartTime
                    # multiply with the sonic speed (34300 cm/s)
                    # and divide by 2, because there and back
                    distance = (TimeElapsed * 34300) / 2
                    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
                    #print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature,humidity))
                    break
	
        #    humidity,temperature = Adafruit_DHT.read_retry(sensor, pin)
         #   print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature,humidity))
        self.wfile.write(html.format(temp[5:], temp[5:7], temp[5:],distance,distance,distance,distance, status,humidity,temperature).encode("utf-8"))


if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        GPIO.cleanup()
