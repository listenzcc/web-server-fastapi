#!/bin/bash

# https://tailwindcss.com/docs/installation

# Set path for newer npm, node and npx
PATH=/home/zcc/nfsHome/usr/node-v20.14.0-linux-x64/bin:$PATH

# Install package
npm install -D tailwindcss
npm install -D @tailwindcss/forms
npm install -D @tailwindcss/typography

npm install @fontsource/space-grotesk

# Initialize config
npx tailwindcss init