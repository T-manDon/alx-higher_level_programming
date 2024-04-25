#!/bin/bash
# a Bash script which takes URL and displays all HTTP methods accepted in the serve
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
