from django.shortcuts import render

import requests
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
github_token = os.environ.get('GITHUB_TOKEN')
username = "aberguecio"

def add_github_to_known_hosts():
    known_hosts_file = os.getcwd()  # Specify the path to your known_hosts file
    
    # Execute the ssh-keyscan command
    process = subprocess.run(['ssh-keyscan', '-t', 'rsa', 'github.com'], capture_output=True, text=True)
    
    if process.returncode == 0:
        # Append the scanned host key to the known_hosts file
        with open(known_hosts_file, 'a') as f:
            f.write(process.stdout)
        print("GitHub has been added to known_hosts.")
    else:
        print("Failed to scan GitHub host key.")

def set_token():
    root_directory = os.getcwd()
    subprocess.run(['git', '-C', root_directory, 'config', 'user.name', "aberguecio"])
    subprocess.run(['git', '-C', root_directory, 'config', 'user.password', github_token])
    remote_url = f"git@github.com:{username}/Git-Pusher.git"
    subprocess.run(['git', '-C', root_directory, 'remote', 'set-url', 'origin', remote_url])

def git_push(request):
    print("__________________START___________________\n")
    remote_repository = "origin"
    branch = "main"

    # Add and commit changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Automatic commit"])
    print("1\n")
    # Push changes to the remote repository
    subprocess.run(["git", "push", remote_repository, branch], env={"GIT_SSH_COMMAND": f"ssh -i {os.getcwd()}/id_ed25519.pub"})
