#!/usr/bin/python3
"""takes in a letter and sends a POST request to a url."""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    data = {'letter': q}
    r = requests.post(url, data=data)
    try:
        if r.json == {}:
            print("No result")
        else:
            print('[{r.json.get("id")}] {r.json.get("name")}')
    except ValueError:
        print("Not a valid JSON")    
