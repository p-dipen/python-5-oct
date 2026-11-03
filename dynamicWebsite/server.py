# import http 
from http.server import  HTTPServer, BaseHTTPRequestHandler
from database import getAllData
class SimpleRequestHandler(BaseHTTPRequestHandler):
    # handle get requests
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = """
        <html>
        <head>
            <title>My Contact Book</title>
        </head>
        <body>
            <h2>My Contact book</h2>

        """

        for contact in getAllData():
            print(contact)
            html += f"<li><strong>{contact['name']} : {contact['number']}</li>"

        html += """
            </ul>
            </body>
            </html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == '__main__':
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print("Server running on port 8001... Press Ctrl+C to stop.")
    httpd.serve_forever()
