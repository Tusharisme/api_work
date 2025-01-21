import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Load the data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Parse query parameters
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/api":
            query_params = parse_qs(parsed_path.query)
            names = query_params.get("name", [])

            # Get marks for the requested names
            marks = [student["marks"] for student in data if student["name"] in names]

            # Send JSON response
            response = {"marks": marks}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            # Return 404 for unsupported paths
            self.send_error(404, "Path not found")
