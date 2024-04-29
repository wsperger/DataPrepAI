import os

# Define the directory structure
repo_structure = {
    "DataPrepAI": {
        ".env": "# Environment variables go here",
        "docker-compose.yml": "version: '3.8'\n\nservices:\n  # Define services here",
        "docker-compose.cloud.yml": "version: '3.8'\n\nservices:\n  # Define cloud services here",
        "README.md": "# DataPrepAI\n\n## Overview\nComplete with your project's overview.",
        "app": {
            "Dockerfile": "# Use an official Python runtime as a parent image",
            "src": {},
            "templates": {},
        },
        "runtime": {
            "Dockerfile": "# Use an official Python runtime as a parent image",
            "scripts": {},
        },
        "db": {
            "sqlite": {
                "init.sql": "-- SQL database initialization commands go here"
            },
            "redis": {},
        },
        "data": {},
        "api": {
            "Dockerfile": "# Dockerfile for API service",
            "src": {},
        }
    }
}

def create_dir_structure(base_path, structure):
    """ Recursively create directory structure and files with content. """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # It's a directory, create it and recurse
            os.makedirs(path, exist_ok=True)
            create_dir_structure(path, content)
        else:
            # It's a file, create it and write content
            with open(path, 'w') as f:
                f.write(content)

# Set the base path where you want to create the structure (e.g., current directory)
base_path = os.getcwd()

# Create the directory structure
create_dir_structure(base_path, repo_structure)

print("Repository structure created successfully.")
