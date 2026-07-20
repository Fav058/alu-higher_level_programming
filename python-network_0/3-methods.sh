#!/bin/bash
# Displays the HTTP methods a server accepts
curl -sI "$1" | grep Allow | cut -d: -f2 | tr -d ' '
