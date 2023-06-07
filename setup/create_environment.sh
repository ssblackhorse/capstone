#!/bin/bash

# Create Docker volumes and networks
docker volume create swag
docker volume create classes
docker volume create ctfd
docker volume create portainer_data
docker network create swag_default

# Check if volumes are created successfully
if [ $? -eq 0 ]; then
  echo "Docker volumes created successfully."
else
  echo "Failed to create Docker volumes."
fi