#!/bin/bash
some_command
if [ $? -ne 0 ]; then
        echo "Command failed"
        exit 1
fi