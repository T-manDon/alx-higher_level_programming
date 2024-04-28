#!/usr/bin/python3
"""
Script takes in the URL, makes a reques and displays
the value of the X-Request-Id variable.
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        value = html.get('X-Request-Id')
        print(value)
