# SERVER - receives requests from the client and sends back replies
# Run with:  python3 server.py   then open http://localhost:8000
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import logic

class Handler(BaseHTTPRequestHandler):

    def reply(self, content, status=200, kind="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", kind)
        self.end_headers()
        self.wfile.write(content.encode())

    def do_GET(self):
        print("Request received: GET", self.path)
        if self.path == "/api/tasks":
            self.reply(json.dumps(logic.get_tasks()))
        else:
            self.reply(open("index.html").read(), kind="text/html")

    def do_POST(self):
        print("Request received: POST", self.path)
        size = int(self.headers["Content-Length"])
        title = json.loads(self.rfile.read(size))["title"]
        if logic.add_task(title):
            self.reply(json.dumps({"message": "Task added"}), 201)
        else:
            self.reply(json.dumps({"message": "Task cannot be empty"}), 400)

print("Server running at http://localhost:8000")
ThreadingHTTPServer(("localhost", 8000), Handler).serve_forever()
