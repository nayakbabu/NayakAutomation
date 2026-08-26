#!/bin/bash
#indexed array script

servers=("web1" "web2" "db1")
echo "${servers[0]}"
echo "${servers[@]}"
echo "${#servers[@]}"

for server in "${servers[@]}";do
        echo "Checking $server"
done

#associative array (bash 4+, like a dictionary)
declare -A server_ips
server_ips["web1"]="10.0.1.10"
server_ips["db1"]="10.0.1.20"
echo "${server_ips[web1]}"

for key in "${!server_ips[@]}"; do
        echo "$key -> ${server_ips[$key]}"
done