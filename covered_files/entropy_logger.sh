#!/bin/bashs
while true; do
  ts=$(date +%s%N)
  ent=$(cat /proc/sys/kernel/random/entropy_avail)
  echo "$ts,$ent" >> "$/var/log/entropy_avail.csv"
  sleep 0.01
done
