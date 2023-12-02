#!/usr/bin/python3
"""
Displays X-Request-Id header variable of a request to a given URL.
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except IndexError:
        pass
