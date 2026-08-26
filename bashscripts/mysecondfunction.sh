#!/bin/bash

greet() {
        local name=$1
        local age=$2
        echo "Hello $name, your age is $age"

}
greet "Satya" "34"