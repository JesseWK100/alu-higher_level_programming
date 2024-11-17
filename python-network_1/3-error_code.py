#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response decoded in UTF-8.
If an HTTP error occurs, it handles the exception and prints the error code.

It uses the `urllib` and `sys` packages.
"""

import urllib.request
import urllib.error
import sys

def fetch_url(url):
    """
    Sends a request to the specified URL and displays the response body (decoded in UTF-8).
    If an HTTP error occurs, prints the error code.
    
    Args:
        url (str): The URL to send the request to.
    """
    try:
        # Open the URL and fetch the response
        with urllib.request.urlopen(url) as response:
            # Read the response body and decode it as utf-8
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP error and print the error code
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    """
    Main entry point of the script.
    
    This block:
        1. Retrieves the URL from the command-line argument.
        2. Calls the `fetch_url` function to fetch the URL and display the response or error.
    """
    # Get URL from the command line argument
    url = sys.argv[1]
    fetch_url(url)
