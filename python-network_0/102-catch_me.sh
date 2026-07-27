#!/bin/bash
# Requests /catch_me with a browser-like User-Agent to get past the bot check.
curl -s -A "Mozilla/5.0" 0.0.0.0:5000/catch_me
