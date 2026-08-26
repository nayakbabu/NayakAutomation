#!/bin/bash
declare -A ports

ports["http"]=80
ports["https"]=443
ports["ssh"]=22
ports["ftp"]=21
ports["pesit"]=1761
ports["AS2"]=5443

for service in "${!ports[@]}"; do
        echo "Service $service uses port ${ports[$service]}"
done