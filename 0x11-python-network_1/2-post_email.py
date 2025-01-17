#!/usr/bin/python3
"""POST an email and display body of the response
"""
import sys
from urllib.request import Request, urlopen
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
