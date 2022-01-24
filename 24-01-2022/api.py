import http.server
import socketserver
import json

PORT = 5050

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path =='/api':
            self.path = 'api_data.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

        
    def do_POST(self):
        # - request -
        
        content_length = int(self.headers['Content-Length'])
        #print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None
            
        print(input_data)
        
        # - response -
        
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        json_file = open("server_client_data.json", "r")
        python_data = json.load(json_file)
        json_data = json.dumps(python_data)

        self.wfile.write(json_data.encode('utf-8'))


Handler = MyHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Starting http://0.0.0.0:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Stopping by Ctrl+C")
    httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use` 
