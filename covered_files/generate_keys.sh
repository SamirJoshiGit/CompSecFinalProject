#!/bin/bash

CSV_OUT="rsa_keys.csv"
if [ ! -f "$CSV_OUT" ]; then
    echo "index,source,entropy,timegenerated,modulus,SHAKEY" > "$CSV_OUT"
fi
for i in $(seq 1 500); do
    PRIV=$(mktemp)
    PUB=$(mktemp)
    ENTROPY=$(cat /proc/sys/kernel/random/entropy_avail)
    START=$(date +%s%N)
    openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out "$PRIV" 2>/dev/null
    openssl pkey -in "$PRIV" -pubout -out "$PUB" 2>/dev/null
    END=$(date +%s%N)
    GEN_TIME_MS=$(( (END - START) / 1000000 ))
    MOD_HEX=$(openssl rsa -pubin -in "$PUB" -noout -modulus | cut -d= -f2)
    HASH=$(openssl pkey -pubin -in "$PUB" -outform DER| sha256sum | awk '{print $1}')
    echo "$i,baseline,$ENTROPY,$GEN_TIME_MS,$MOD_HEX,$HASH" >> "$CSV_OUT"
    rm -f "$PRIV" "$PUB"
done
