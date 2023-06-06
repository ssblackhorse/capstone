import subprocess

def create_docker_volume(volume_name):
    try:
        subprocess.run(['docker', 'volume', 'create', volume_name], check=True)
        print(f"Docker volume '{volume_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating docker volume '{volume_name}': {e}")

def create_docker_network(network_name):
    try:
        subprocess.run(['docker', 'network', 'create', network_name], check=True)
        print(f"Docker network '{network_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating docker network '{network_name}': {e}")

def clone_repository(repo_url, destination):
    try:
        subprocess.run(['git', 'clone', repo_url, destination], check=True)
        print(f"Repository cloned successfully to '{destination}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

def main():
    create_docker_volume('swag')
    create_docker_volume('classes')
    create_docker_volume('ctfd')
    create_docker_volume('portainer_data')
    create_docker_network('swag_default')
    clone_repository('https://github.com/CTFd/CTFd', '/var/lib/docker/volumes/ctfd')

if __name__ == '__main__':
    main()
