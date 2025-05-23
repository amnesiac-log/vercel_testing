from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Parse query parameters
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        names = query_params.get('name', [])
        
        # Load data
        with open('q-vercel-python.json', 'r') as f:
            data = json.load(f)
        
        # Build name to marks mapping
        name_to_marks = {item["name"]: item["marks"] for item in data}
        
        # Get marks for requested names
        marks = [name_to_marks.get(name, None) for name in names]
        
        # Return response
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode())
