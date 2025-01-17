#!/usr/bin/python3
"""script to fetch resources from a url"""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        content = response.read()
        print(f"Body response:")
        print(f"    - type: {type(content)}")
        print(f"    - content: {content}")
        print(f"    - utf8 content: {content.decode('utf-8')}")
