import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"


DUMMY_RESPONSE = """
<html>
<head>
<title>Python Test</title>
</head>

<body>
Test page...success.
</body>
</html>
"""

class MyHandler(CGIHTTPRequestHandler):

    def __init__(self,req,client_addr,server):
        CGIHTTPRequestHandler.__init__(self,req,client_addr,server)

def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.send_header("Content-length", len(DUMMY_RESPONSE))
    self.end_headers()
    self.wfile.write(DUMMY_RESPONSE)







if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
