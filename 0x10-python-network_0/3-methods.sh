#!/bin/bash
# Script that takes an URL and shows allowed options.
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
