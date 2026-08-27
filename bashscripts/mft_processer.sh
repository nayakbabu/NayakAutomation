#!/bin/bash
set -euo pipefail

#-----------------------------------------------------------------------------------------------------------------------------------
#Function Name: process_incoming_file
#Purpose: Validate file size and its externsions then routes to archive or quarantine
#Written By: Nayak Satya MFT certifed infra specialist
#-----------------------------------------------------------------------------------------------------------------------------------

process_incoming_file() {
    local input_file="$1"
    local archive_dir="./archive"
    local quarantine_dir="./quarantine"
# Ensure target directory exists
    mkdir -p "$archive_dir" "$quarantine_dir"

    if [[ ! -e "$input_file" ]]; then
        echo "[ALERT] File '$input_file' is missing."
        return 1
    fi

    if [[ ! -f "$input_file" || ! -s "$input_file" ]]; then
        echo "[ALERT] File '$input_file' is not a non-empty regular file. Quarantining."
        mv "$input_file" "$quarantine_dir/"
        return 1
    fi

    local lower="${input_file,,}"
    if [[ "$lower" == *.csv || "$lower" == *.txt ]]; then
        echo "[SUCCESS] File '$input_file' valid. Moving to archive."
        mv "$input_file" "$archive_dir/"
        return 0
    fi

    echo "[REJECTED] Invalid extension on '$input_file'. Quarantining."
    mv "$input_file" "$quarantine_dir/"
    return 1
}

if [[ $# -lt 1 || -z "${1:-}" ]]; then
    echo "Usage: $0 <file>" >&2
    exit 2
fi
#--- SCRIPT EXECUTION STARTS HERE ---
# Call the function with proper test data and argument, you have to create a valid csv or txt file
process_incoming_file "$1"