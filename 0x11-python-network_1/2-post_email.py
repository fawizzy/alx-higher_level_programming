#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    full_url = url + '?' + data
    with urllib.request.urlopen(full_url) as response:
        html = response.read()
    print(html)