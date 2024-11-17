#!/usr/bin/python3
"""
Script that takes a URL, sends a request to the URL, 
and displays the size of the body of the response in bytes.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-body_size.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(len(response.content))
    except requests.RequestException as e:
        print(f"Error: {e}")
