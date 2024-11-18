#!/usr/bin/python3
"""
This script fetches the content of the URL https://alu-intranet.hbtn.io/status
using the `requests` package and displays the response in a specific format.

Usage:
    Execute the script directly to see the formatted response.

Output Example:
    Body response:
        - type: <class 'str'>
        - content: OK
"""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    # Fetch the response from the URL
    response = requests.get(url)
    content = response.text

    # Display the formatted output
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
