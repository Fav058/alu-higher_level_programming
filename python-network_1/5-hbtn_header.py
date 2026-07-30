#!/usr/bin/python3
"""Displays X-Request-Id header value using requests"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
