#!/bin/bash

# Check if Docker is installed
if ! [ -x "$(command -v docker)" ]; then
    echo "Docker is not installed. Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    echo "Docker has been installed."
else
    echo "Docker is already installed."
fi

# Check if Docker Compose is installed
if ! [ -x "$(command -v docker-compose)" ]; then
    echo "Docker Compose is not installed. Installing Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo "Docker Compose has been installed."
else
    echo "Docker Compose is already installed."
fi

# Post-installation recommendations
echo "Performing post-installation steps..."
# Enable Docker to start on boot
sudo systemctl enable docker
# Start Docker service
sudo systemctl start docker
# Add current user to the 'docker' group
sudo usermod -aG docker $USER
# Display Docker version
docker --version
# Display Docker Compose version
docker-compose --version
echo "Post-installation steps have been completed."