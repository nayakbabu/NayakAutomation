#!/bin/bash
get_disk_usage() {
        local usage
        usage=$(df -h /|awk 'NR==2{print $5}'|tr -d '%')
        echo "$usage"

}
DISK=$(get_disk_usage)
echo "Disk is at $DISK%"