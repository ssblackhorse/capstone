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

# Clone CTFd repository
echo "Cloning CTFd repository to the ctfd volume..."
git clone https://github.com/CTFd/CTFd.git /var/lib/docker/volumes/ctfd/
echo "CTFd repository cloned successfully."

# Make other scripts executable
echo "Making the other scripts executable..."
chmod +x create_courses.sh
chmod +x user_info.sh
chmod +x $PWD/troubleshooting/waiting_for_db_error.sh

# Add dockeruser and grant sudo privileges
echo "Creating the docker user and updating it's permissions..."
sudo adduser dockeruser
sudo usermod --password $(openssl rand -base64 12) dockeruser
sudo adduser dockeruser sudo

# Add dockeruser to the docker group
sudo usermod -aG docker dockeruser

# Switch to the docker group
newgrp docker

echo "New user details:"
echo "Username: dockeruser"
echo "Password: $(sudo cat /etc/shadow | grep dockeruser | awk -F':' '{print $2}')"

echo "Change to this new user if you haven't already by 'su dockeruser'"
