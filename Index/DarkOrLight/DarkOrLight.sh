#!/bin/bash

query=$1

# Check=`defaults read -g AppleInterfaceStyle`

if [ "$query" = "dark" ]; then
	dark='true'
elif [ "$query" = "light" ]; then
	dark='false'
else
	dark='not dark mode'
fi

Script="tell app \"System Events\" to tell appearance preferences to set dark mode to $dark"

osascript -e "$Script"
