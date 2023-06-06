import os
import subprocess

def create_folders(basepath, username):
    try:
        subprocess.run(['sudo', 'mkdir', '-p', f'{basepath}/uploads'], check=True)
        subprocess.run(['sudo', 'mkdir', '-p', f'{basepath}/logs'], check=True)
        subprocess.run(['sudo', 'mkdir', '-p', f'{basepath}/redis/data'], check=True)
        subprocess.run(['sudo', 'mkdir', '-p', f'{basepath}/db/mysql'], check=True)
        subprocess.run(['sudo', 'chown', '-R', f'{username}:{username}', basepath], check=True)
        print("Folder structure created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating folder structure: {e}")

def rename_and_modify_config_file(coursename):
    source_file = "/config_files/course.subdomain.conf"
    destination_file = f"/config_files/{coursename}.subdomain.conf"

    try:
        subprocess.run(['sudo', 'cp', source_file, destination_file], check=True)
        print(f"Config file copied and renamed to '{destination_file}' successfully.")

        with open(destination_file, 'r') as file:
            content = file.read()

        modified_content = content.replace('<container_name>', coursename)

        with open(destination_file, 'w') as file:
            file.write(modified_content)

        print(f"Config file modified successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error copying/renaming or modifying the config file: {e}")

def copy_config_file_to_swag(coursename):
    source_file = f"/config_files/{coursename}.subdomain.conf"
    destination_file = f"/var/lib/docker/volumes/swag/config/proxy-confs/{coursename}.subdomain.conf"

    try:
        subprocess.run(['sudo', 'cp', source_file, destination_file], check=True)
        print(f"Config file copied to '{destination_file}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error copying the config file to '{destination_file}': {e}")

def restart_swag_container():
    try:
        subprocess.run(['sudo', 'docker', 'restart', 'swag'], check=True)
        print("Swag container restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting the Swag container: {e}")

def main():
    coursename = input("Enter the course name: ")
    basepath = f"/var/lib/docker/volumes/classes/{coursename}"
    username = 'dockeruser'
    
    create_folders(basepath, username)
    rename_and_modify_config_file(coursename)
    copy_config_file_to_swag(coursename)
    restart_swag_container()

if __name__ == '__main__':
    main()
