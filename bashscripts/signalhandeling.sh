#!/bin/bash
cleanup() {
        echo "Script interrupted or exiting -- cleaning up..."
        rm -f /tmp/mylockfile
        exit 1
}
trap cleanup SIGINT SIGTERM EXIT

touch /tmp/mylockfile
echo "Working...Press Ctrl+C to test trap"
sleep 30