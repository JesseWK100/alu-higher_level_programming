#!/usr/bin/python3
"""
This script fetches the content of the URL https://alu-intranet.hbtn.io/status
using the `requests` package and displays the response in a specific format.

Output Example:
    Body response:
        - type: <class 'str'>
        - content: Custom status
"""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: Custom status")
