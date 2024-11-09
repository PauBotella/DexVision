#!/bin/bash

folder="Sprites"
width=250

for file in "$folder"/*.gif; do
    if [[ -f "$file" ]]; then
        echo "Processing $file ..."
        gifsicle --resize-width $width "$file" -o "$file"
        echo "$file resized."
    fi
done