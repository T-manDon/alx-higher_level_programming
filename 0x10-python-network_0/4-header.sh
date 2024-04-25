#!/bin/bash
# The cript takes the URL as an argument, issue GET request to the URL, and display the response
curl -sX GET -H "X-School-User-Id: 98" "$1"
