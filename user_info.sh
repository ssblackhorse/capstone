#!/bin/bash

# Print public IP
public_ip=$(curl -s ifconfig.me)
echo "Public IP: $public_ip"

# Print address to portainer
echo "Address to Portainer: https://$public_ip:9443"

# Print PGID for dockeruser
pgid=$(id -g dockeruser)
echo "PGID for dockeruser: $pgid"

# Print PUID for dockeruser
puid=$(id -u dockeruser)
echo "PUID for dockeruser: $puid"