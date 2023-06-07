#!/bin/bash

# Prompt the user for the course name
read -p "Enter the course name: " coursename

# Define the base path
basepath="/var/lib/docker/volumes/classes/$coursename"

# Create the folders using sudo
sudo mkdir -p "$basepath/uploads"
sudo mkdir -p "$basepath/logs"
sudo mkdir -p "$basepath/redis/data"
sudo mkdir -p "$basepath/db/mysql"

# Change ownership of the folders to the current user
sudo chown -R $USER:$USER "$basepath"

# Copy and rename the configuration file
sudo cp "/root/config_files/course.subfolder.conf" "/var/lib/docker/swag/config/proxy-confs/$coursename.subfolder.conf"

# Replace <container_name> with the course name in the copied file
sudo sed -i "s/<container_name>/$coursename/g" "/var/lib/docker/swag/config/proxy-confs/$coursename.subfolder.conf"

# Restart the 'swag' Docker container
sudo docker restart swag

# Display success message
echo "Folder structure created, configuration file copied, and 'swag' Docker container restarted successfully."

# Prompt for DNS configuration
echo "Please make sure that you have configured your DNS to have a CNAME record which points to https://yourdomain.tld/${coursename}."
