#!/usr/bin/python3
"""
Python script takes in a URL, request url displays
the X-Request-Id variable in the header of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers.get("X-Request-Id")
    print(value)
