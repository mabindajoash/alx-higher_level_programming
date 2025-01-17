#!/usr/bin/python3
"""sends a request to the URL and displays
the value of the X-Request-Id variable
"""
import sys
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
