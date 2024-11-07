#!/bin/bash

folder="/home/pau/proyects/DexVision/AnimatedSprites"

# Loop through each .gif file in the folder
for file in "$folder"/*.gif; do
    if [[ -f "$file" ]]; then
        echo "Processing $file ..."
        # Run gifsicle to resize the width to 250 pixels
        gifsicle --resize-width 250 "$file" -o "$file"
        echo "$file resized."
    fi
done

echo "Process completed."
