#!/bin/bash
get_memory_usage() {
        local usage
        usage=$(free -m | awk 'NR==2{printf "%.0f", $3/$2*100}')
        echo "$usage"
}
MEMORY=$(get_memory_usage)
echo "Memory usage is at $MEMORY%"