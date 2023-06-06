import os

def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print("File renamed successfully.")
    except OSError as e:
        print(f"Error renaming file: {e}")

def main():
    old_path = "/required_files/example.env"
    new_path = "/required_files/.env"

    rename_file(old_path, new_path)

if __name__ == '__main__':
    main()
