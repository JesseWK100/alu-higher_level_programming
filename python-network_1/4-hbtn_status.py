#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status
and displays the response body with information about
its type and content.

Usage:
    ./4-hbtn_status.py
"""

import requests

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
