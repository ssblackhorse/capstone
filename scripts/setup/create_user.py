import subprocess
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def create_user(username, password):
    print(f"Creating user: {username}")
    subprocess.run(['sudo', 'useradd', '-m', username], check=True)
    subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{password}", encoding='utf-8', check=True)
    print(f"User '{username}' created successfully.")

def run_commands(username):
    print("Running commands...")
    subprocess.run(['sudo', 'adduser', username, 'sudo'], check=True)
    subprocess.run(['sudo', 'usermod', '-aG', 'docker', username], check=True)
    subprocess.run(['newgrp', 'docker'], check=True)
    print("Commands executed successfully.")

def main():
    username = "dockeruser"
    password = generate_password()
    
    create_user(username, password)
    run_commands(username)

if __name__ == '__main__':
    main()
