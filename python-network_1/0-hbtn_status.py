#!/usr/bin/python3
"""
This script fetches the status from https://alu-intranet.hbtn.io/status
using the urllib package and displays the body of the response.
"""

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
