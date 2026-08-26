#!/bin/bash

greet() {
        local name=$1
        local age=$2
        local city=$3
        echo "Hello $name, your age is $age , You belongs to $city"

}
greet "Nayak" "34" "Sofia"