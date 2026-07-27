#!/bin/bash
# Sends a POST request with the contents of a file as the JSON body.
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
