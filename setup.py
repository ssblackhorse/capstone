import os
import subprocess

def make_script_executable(script_path):
    try:
        subprocess.run(['chmod', '+x', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error making script '{script_path}' executable: {e}")

def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script '{script_path}': {e}")

def main():
    scripts = [
        'docker_installation.py',
        'setup_directories.py',
        'rename_env.py',
        'create_user.py',
        'user_info.py'
    ]

    script_directory = '/capstone/scripts/setup'

    for script in scripts:
        script_path = os.path.join(script_directory, script)
        make_script_executable(script_path)
        run_script(script_path)

if __name__ == '__main__':
    main()
