from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head>
            <title>Phone2Cloud Server</title>
        </head>
        <body style="font-family:Arial;text-align:center;padding-top:100px;">
            <h1>🚀 Server is Running</h1>
            <p>Phone2Cloud backend is online.</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)

    print("🚀 Server running on http://localhost:8000")
    print("🌐 LAN access: http://YOUR_IP:8000")

    server.serve_forever()
