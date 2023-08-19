import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

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

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
           <html><head><title>LED ON & OFF</title>
           </head>
           <body style="width:960px; margin: 20px auto;">
           <header style="display:block;background-color:lavender;text-align:center;">
           <h1>LED ON & OFF</h1>
           <p>By Raspberry pi</p>
           <p>Using Led</p></header><div style="display:flex;text-align:center;"><div class="card" style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);transition: 0.3s;width:50%;"><div class="container" style="padding: 2px 16px;">
           <h1>Welcome to my Raspberry Pi</h1>
           <p>Current GPU temperature is {}</p>
           <form action="/" method="POST">
               Turn LED :
               <button type="submit" name="submit" value="On" style="width:60px;height:80px;"><img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.billfrymire.com%2Fgallery%2Fweblarge%2Fincandescent-lightbulb-glow.jpg&f=1&nofb=1&ipt=5ab9d02a67f6b09aeddb21aa261cf077948c54e440235fa99376bad1d0936d5b&ipo=images" style="width:50px;height:70px;"></button>
               <button type="submit" name="submit" value="Off" style="width:60px;height:80px;"><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fjooinn.com%2Fimages%2Fisolated-light-bulb-1.jpg&f=1&nofb=1&ipt=69d0ffe4372dbe3121d3e96914322a4a9cf0722f2f04b0799ed67103028896da&ipo=images" style="width:50px;height:70px;"></button>
           </form></div></div><div class="card" style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);transition: 0.3s;width:50%;"><div class="container" style="padding: 2px 16px;">
           <h1>Welcome to my Raspberry Pi</h1>
           <form action="" method="POST">
               Turn LED :
               <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.billfrymire.com%2Fgallery%2Fweblarge%2Fincandescent-lightbulb-glow.jpg&f=1&nofb=1&ipt=5ab9d02a67>
               <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fjooinn.com%2Fimages%2Fisolated-light-bulb-1.jpg&f=1&nofb=1&ipt=69d0ffe4372dbe3121d3e96914322a4a9cf>
           </form></div></div></div>
           </body>
           </html>
        '''
        temp = os.popen("vcgencmd measure_temp").read()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):
        """ do_POST() can be tested using curl command
            'curl -d "submit=On" http://server-ip-address:port'
        """
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length).decode("utf-8")  # Get the data
        post_data = post_data.split("=")[1]  # Only keep the value

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)

        if post_data == 'On':
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)
        print("LED is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url


if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
