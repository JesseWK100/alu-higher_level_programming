#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email as a parameter, and
displays the body of the response decoded in UTF-8.
It uses the urllib and sys packages.
"""

import urllib.parse
import urllib.request
import sys

def post_email(url, email):
    """Send a POST request with email as parameter and display the response body."""
    # Create a dictionary with the email parameter
    data = {'email': email}
    # Encode the dictionary into URL-encoded format
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    # Send the POST request with the encoded data
    with urllib.request.urlopen(url, data=encoded_data) as response:
        # Read the response and decode it as utf-8
        body = response.read().decode('utf-8')
        print(f"Your email is: {email}")
        print(body)

if __name__ == "__main__":
    # Get URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
