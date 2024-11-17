#!/usr/bin/python3
"""
This script fetches the status of a URL and displays its response body with
the requested format.

It uses the urllib package for fetching the content.
"""

import urllib.request

def fetch_status():
    """Fetch the content from the URL and display the response body."""
    url = 'https://alu-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        # Printing the body content with the required formatting
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
