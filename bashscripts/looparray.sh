#!/bin/bash
services=("nginx" "mysql" "axway" "docker")

for svc in "${services[@]}"; do
        echo "Service name: $svc"
done