#!/bin/bash
# Takes the URL, gives a GET request to URL, then display the response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
