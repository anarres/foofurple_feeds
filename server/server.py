#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("127.0.0.5", 8005)
handler.cgi_directories = ["/home/katie/prog/foofurple_feeds/server/"]

httpd = server(server_address, handler)
httpd.serve_forever()

