#!/bin/bash
# script sends JSON POST request to the URL in the first argument, and show response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
