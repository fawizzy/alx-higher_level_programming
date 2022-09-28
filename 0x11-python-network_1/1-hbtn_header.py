import sys
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/"
    with urllib.request.urlopen(url) as response:
        header = response.getheaders()
    for i in header:
        print(i)
        print(type(i))