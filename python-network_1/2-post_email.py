#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email as a parameter,
and then displays the body of the response, decoded in UTF-8.

The script uses the `urllib` and `sys` packages to make the request and process
the response.

Usage:
    ./2-post_email.py <URL> <email>

Arguments:
    <URL>   The URL to which the POST request is sent.
    <email> The email to be sent as a parameter in the POST request.

The script will print the email used in the request followed by the body of the response.
"""

import urllib.parse
import urllib.request
import sys

def post_email(url, email):
    """
    Sends a POST request to the specified URL with the given email as a parameter.

    Args:
        url (str): The URL to which the POST request is sent.
        email (str): The email to be included in the POST request as a parameter.

    The function:
        1. Encodes the email as a URL parameter.
        2. Sends the POST request with the encoded email.
        3. Reads and decodes the response body.
        4. Prints the email used and the response body.
    """
    # Create a dictionary with the email parameter
    data = {'email': email}
    # Encode the dictionary into URL-encoded format
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    # Send the POST request with the encoded data
    with urllib.request.urlopen(url, data=encoded_data) as response:
        # Read the response body and decode it as utf-8
        body = response.read().decode('utf-8')
        print(f"Your email is: {email}")
        print(body)

if __name__ == "__main__":
    """
    The main entry point of the script.
    
    This block:
        1. Retrieves the URL and email from the command-line arguments.
        2. Calls the `post_email` function to send the POST request and display the response.

    It ensures the script behaves as expected when executed directly.
    """
    # Get URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
