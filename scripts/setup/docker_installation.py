import subprocess
import sys

def check_installed(command):
    try:
        subprocess.run([command, '--version'], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_docker():
    print("Installing Docker...")
    subprocess.run(['curl', '-fsSL', 'https://get.docker.com', '-o', 'get-docker.sh'], check=True)
    subprocess.run(['sudo', 'sh', 'get-docker.sh'], check=True)
    print("Docker installed successfully.")

def install_docker_compose():
    print("Installing Docker Compose...")
    subprocess.run(['sudo', 'curl', '-fsSL', '-o', '/usr/local/bin/docker-compose', 'https://github.com/docker/compose/releases/latest/download/docker-compose-Linux-x86_64'], check=True)
    subprocess.run(['sudo', 'chmod', '+x', '/usr/local/bin/docker-compose'], check=True)
    print("Docker Compose installed successfully.")

def perform_post_installation():
    print("Performing post-installation steps...")
    subprocess.run(['sudo', 'groupadd', 'docker'], check=True)
    subprocess.run(['sudo', 'usermod', '-aG', 'docker', '$USER'], check=True)
    subprocess.run(['newgrp', 'docker'], check=True)
    subprocess.run(['sudo', 'systemctl', 'enable', 'docker'], check=True)
    print("Post-installation steps completed successfully.")

def main():
    if not check_installed('docker'):
        install_docker()
        perform_post_installation()
    else:
        print("Docker is already installed.")

    if not check_installed('docker-compose'):
        install_docker_compose()
    else:
        print("Docker Compose is already installed.")

if __name__ == '__main__':
    main()
