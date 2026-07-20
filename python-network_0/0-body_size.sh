#!/bin/bash
# Displays the size of the body response in bytes

curl -s "$1" | wc -c
