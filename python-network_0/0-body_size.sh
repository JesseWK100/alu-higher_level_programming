#!/bin/bash
# Script that takes a URL, sends a request, and displays the size of the response body in bytes

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -s -o /dev/null -w "%{size_download}\n" "$1"
