#!/bin/bash
# Gives a request to 0.0.0.0:5000/catch_me causing the server to give the message You got me!, in response.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
