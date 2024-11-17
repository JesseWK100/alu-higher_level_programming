#!/bin/bash
# Send a request to the provided URL and display the size of the response body
curl -s -o /dev/null -w "%{size_download}\n" "$"
