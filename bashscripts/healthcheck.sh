#!/bin/bash
LOGFILE=~/cloudelabday1/healthcheck.log
echo "=== $(date) ===" >> $LOGFILE

#disk check

DISK_USAGE=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')
echo "Disk usage: ${DISK_USAGE}%" >> "$LOGFILE"
if [ "$DISK_USAGE" -gt 80 ]; then
  echo "WARNING: Disk usage is ${DISK_USAGE}%" >> "$LOGFILE"
fi

#memory check
echo "--- Memory ---" >> "$LOGFILE"

free -h >> "$LOGFILE"

#top 5 cpu process
echo "--- Top 5 CPU processes ---" >> "$LOGFILE"
ps aux --sort=-%cpu | head -6 >> "$LOGFILE"

echo "" >> "$LOGFILE"