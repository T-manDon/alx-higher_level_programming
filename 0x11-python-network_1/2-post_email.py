#!/usr/bin/python3
"""
The script takes URL and an email, then issue a POST request to passed
URL with email displays the body of the response
(decoded in utf-8)."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {
        "email": email
    }
    query_string = urllib.parse.urlencode(param)
    data = query_string.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        # If you do not pass the data argument, urllib uses a GET request.
        # One way in which GET and POST requests differ is that POST requests
        # often have "side-effects".
        response_text = response.read().decode("utf-8")
        print(response_text)
