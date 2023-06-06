#!/bin/bash

read -p "Enter the class name: " classname

# Create class folder
mkdir "$classname"
cd "$classname"

# Create subfolders
mkdir uploads logs redis db
mkdir redis/data db/mysql

echo "Folder structure created successfully!"
