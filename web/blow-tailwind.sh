#!/bin/bash

# Set path for newer npm, node and npx
PATH=/home/zcc/nfsHome/usr/node-v20.14.0-linux-x64/bin:$PATH

# Update the settings that are recommended
# npx update-browserslist-db@latest

# Watch the folder and keep it up-to-date
npx tailwindcss -i ./src/input.css -o ./static/css/style.css --watch