#!/usr/bin/env python3
"""
Custom Development Server for SDS Book Documentation

This server provides GitHub Pages-compatible clean URL handling for local development.
It automatically serves HTML files without requiring the .html extension.

Features:
- Clean URLs: /page serves page.html
- Directory indexes: /directory/ serves directory/index.html
- Query parameter preservation
- CORS headers for development
- Static file serving (CSS, JS, images)
- Proper error handling

Usage:
    python3 code/serve.py [port]
    
Examples:
    python3 code/serve.py          # Serves on port 8080
    python3 code/serve.py 3000     # Serves on port 3000
"""

import http.server
import socketserver
import os
import sys
import mimetypes
from urllib.parse import unquote, urlparse
from pathlib import Path

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler that provides clean URL support like GitHub Pages."""
    
    def __init__(self, *args, **kwargs):
        # Set the directory to serve from
        super().__init__(*args, directory='build', **kwargs)
    
    def do_GET(self):
        """Handle GET requests with clean URL resolution."""
        try:
            # Parse the requested URL
            parsed_url = urlparse(self.path)
            url_path = unquote(parsed_url.path)
            query_string = parsed_url.query
            
            # Remove leading slash for file system operations
            clean_path = url_path.lstrip('/')
            
            # Try to resolve the file
            resolved_file = self.resolve_file_path(clean_path)
            
            if resolved_file:
                # Reconstruct the path for the parent handler
                self.path = '/' + resolved_file
                if query_string:
                    self.path += '?' + query_string
                
                # Add CORS headers for development
                self.add_cors_headers = True
                return super().do_GET()
            else:
                # File not found
                self.send_error(404, f"File not found: {url_path}")
                
        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")
    
    def resolve_file_path(self, requested_path):
        """
        Resolve a clean URL to an actual file path.
        
        Args:
            requested_path (str): The path without leading slash
            
        Returns:
            str or None: The resolved file path, or None if not found
        """
        base_dir = Path('build')
        
        # List of paths to try, in order of preference
        path_attempts = []
        
        # 1. Exact path (for existing files and static assets)
        if requested_path:
            path_attempts.append(requested_path)
        
        # 2. Add .html extension (main case for clean URLs)
        if requested_path and not requested_path.endswith('.html'):
            path_attempts.append(requested_path + '.html')
        
        # 3. Try as directory with index.html
        if not requested_path or requested_path.endswith('/'):
            # Root or directory ending with /
            index_path = requested_path + 'index.html' if requested_path else 'index.html'
            path_attempts.append(index_path)
        else:
            # Try adding /index.html to the path
            path_attempts.append(requested_path + '/index.html')
        
        # Test each path attempt
        for attempt in path_attempts:
            full_path = base_dir / attempt
            if full_path.is_file():
                return attempt
        
        return None
    
    def end_headers(self):
        """Add CORS headers for development."""
        if hasattr(self, 'add_cors_headers'):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom log format with clean URLs."""
        # Only log successful requests and errors, not every asset
        if '200' in str(args) or '404' in str(args) or '500' in str(args):
            print(f"[{self.log_date_time_string()}] {format % args}")

class ReusableTCPServer(socketserver.TCPServer):
    """TCP Server that allows port reuse."""
    allow_reuse_address = True

def main():
    """Start the development server."""
    # Parse command line arguments
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"❌ Invalid port number: {sys.argv[1]}")
            print("Usage: python3 code/serve.py [port]")
            sys.exit(1)
    
    # Check if build directory exists
    if not os.path.exists('build'):
        print("❌ Build directory not found!")
        print("Please run 'make all' or 'make [language]' first to build the documentation.")
        sys.exit(1)
    
    # Check if build directory has content
    if not os.listdir('build'):
        print("❌ Build directory is empty!")
        print("Please run 'make all' or 'make [language]' first to build the documentation.")
        sys.exit(1)
    
    try:
        # Create and start the server
        with ReusableTCPServer(("", port), CleanURLHandler) as httpd:
            print("🚀 SDS Development Server")
            print("=" * 50)
            print(f"📍 Server URL: http://localhost:{port}")
            print(f"📁 Serving from: ./build/")
            print()
            print("📖 Available Language Versions:")
            
            # List available language versions
            for lang in ['en', 'fr', 'it', 'es']:
                lang_dir = f"build/{lang}"
                if os.path.exists(lang_dir):
                    print(f"   • {lang.upper()}: http://localhost:{port}/{lang}/")
            
            print()
            print("🔗 URL Shortener:")
            print(f"   • Main: http://localhost:{port}/short.html")
            print(f"   • Test: http://localhost:{port}/short.html?short=github")
            
            print()
            print("✨ Clean URL Examples:")
            if os.path.exists("build/it/P1-PAD/presentazione.html"):
                print(f"   • http://localhost:{port}/it/P1-PAD/presentazione")
            if os.path.exists("build/en/home.html"):
                print(f"   • http://localhost:{port}/en/home")
            
            print()
            print("🛑 Press Ctrl+C to stop the server")
            print("=" * 50)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use!")
            print(f"Try a different port: python3 code/serve.py {port + 1}")
        else:
            print(f"❌ Server error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
