#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email as a parameter,
then displays the body of the response decoded in UTF-8.

The script uses the `urllib` and `sys` packages.

Usage:
    ./2-post_email.py <URL> <email>

Arguments:
    <URL>   The URL to send the POST request to.
    <email> The email to send as a parameter in the POST request.

The script will display the email used in the request followed by the server's response body.
"""

import urllib.parse
import urllib.request
import sys

def post_email(url, email):
    """
    Sends a POST request to the specified URL with the given email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to send as a parameter in the request.

    Sends the POST request and displays the body of the response, decoded in UTF-8.
    Also prints the email that was sent with the request.
    """
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
    """
    Main entry point of the script. Retrieves the URL and email from command-line
    arguments and calls `post_email` to send the POST request and display the response.
    """
    # Get URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
