import http.server
import socketserver
import webbrowser
import os
import sys

# Configuration
PORT = 8080
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Suppress default logging to keep console clean
        pass

def find_free_port(start_port):
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
            port += 1

def main():
    # Change to the directory where the script is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        # Find a free port if 8080 is taken
        import socket
        port = find_free_port(PORT)
        
        url = f"http://localhost:{port}"
        print(f"\n🚀 Oksana's Game of Life is running!")
        print(f"👉 Opening {url} in your browser...")
        print(f"Press Ctrl+C to stop the server.\n")
        
        # Open web browser
        webbrowser.open(url)
        
        # Start server
        with socketserver.TCPServer(("", port), Handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n🛑 Server stopped. Have a productive day!")
                sys.exit(0)
                
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
