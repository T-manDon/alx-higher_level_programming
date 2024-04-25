#!/bin/bash
# The script takes in a URL, the POST request to passed URL
curl -sd "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
