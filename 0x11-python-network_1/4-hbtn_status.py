#!/usr/bin/python3
"""fetch url"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    r.encoding = 'utf-8'
    print("Body response:$")
    print("\t- type: {}$".format(type(r.text)))
    print("\t- content: {}$".format(r.text))
