from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result:':'this is a python test'}
host = ('0.0.0.0', 9527)

class Request(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
  server = HTTPServer(host, Request)
  print('Starting server, listen at: %s:%s' % host)
  server.serve_forever()
