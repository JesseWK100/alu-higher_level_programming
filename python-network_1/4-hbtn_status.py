#!/usr/bin/python3
import requests

url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: Custom status")
