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
        # Concatenating 'OK' and 'Custom status' for demonstration
        combined_content = body + b' Custom status'
        utf8_combined_content = combined_content.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(combined_content)))
        print("\t- content: {}".format(combined_content))
        print("\t- utf8 content: {}".format(utf8_combined_content))
