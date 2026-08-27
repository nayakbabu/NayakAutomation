#!/bin/bash
# Shebang: execution path for the Bash interpreter
set -euo pipefail
# Strict execution mode: exit on error (-e), exit on unset vars (-u), fail pipelines (-o pipefail)

check_disk() {
# Define local function to fetch root partition disk usage percentage
        local usage
        usage=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')
# Get disk stats for / -> extract Use% column from row 2 -> strip % sign
        echo "$usage"
        # Output raw integer value for command substitution
}
DISK=$(check_disk)
# Execute function and capture output into variable
echo "Disk is at $DISK%"
# Display current root disk usage
servers=("web1" "web2" "db1")
# Initialize indexed array with target server names written by Nayak 
echo "${servers[0]}"
echo "${servers[@]}"
echo "${#servers[@]}"


for server in "${servers[@]}";do
# Iterate through each server name in the array written by Nayak 
        echo "Checking $server - Disk usage: ${DISK}%"
        # Print status message for current server
done