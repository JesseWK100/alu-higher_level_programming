#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status
and displays the response body with information about
its type, content, and utf-8 decoded content.

Usage:
    ./0-hbtn_status.py
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
