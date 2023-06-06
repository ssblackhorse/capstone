#!/bin/bash

# Ask user for the course name
read -p "Enter the course name: " coursename

# Stop the Docker containers
docker container stop "$coursename"
docker container stop "$coursename-db-1"

# Remove the MySQL database directory
sudo rm -rf "/var/lib/docker/volumes/classes/$coursename/db/mysql"

# Recreate the MySQL database directory
sudo mkdir -p "/var/lib/docker/volumes/classes/$coursename/db/mysql"

# Start the Docker containers
docker container start "$coursename-db-1"
docker container start "$coursename"

echo "Actions completed successfully."
