from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import json

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api' or self.path == '/api/':
            self.send_response(200)
            self.send_header("Content-type", 'text/json')
            self.end_headers()
            with open('server_client_data.json') as data_file:    
                data = json.load(data_file)
                json_data = json.dumps(data)
                self.wfile.write(bytes((json_data),"utf-8"))

def main():
    PORT = 8000

    try:
        myserver = HTTPServer(('0.0.0.0', PORT), myhandler)
        print("Server started at port:"+str(PORT))
        myserver.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        myserver.socket.close()


if __name__ == '__main__':
    main()
