#!/bin/bash
set -e
CAMERA_SCRIPT="./capture_entropy.sh"
$CAMERA_SCRIPT

HASH=$(cat final_hash.bin)
echo "$HASH" > "camera_hash.bin"

for i in $(seq 1 30); do
    HASH=$(echo -n "$HASH" | sha256sum | awk '{print $1}')
    echo "$HASH" >> "camera_hash.bin"
done

