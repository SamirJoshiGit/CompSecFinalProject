#!/bin/bash
COUNT=20
rm -f frame_*.png combined.hex final_hash.txt
ffmpeg -f video4linux2 -i /dev/video0 -vframes $COUNT frame_%03d.png -y > /dev/null 2>&1
touch combined.hex
for img in frame_*.png; do
    xxd -p "$img" >> combined.hex
done
FINAL_HASH=$(sha256sum combined.hex | awk '{print $1}')
echo "$FINAL_HASH" > final_hash.bin
