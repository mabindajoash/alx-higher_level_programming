#!/usr/bin/env bash
#Display only the status code

curl -s -o /dev/null -w "%{http_code}" $1
