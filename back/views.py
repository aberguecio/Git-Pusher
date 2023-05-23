from django.shortcuts import render

import requests
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
github_token = os.environ.get('GITHUB_TOKEN')
username = "aberguecio"

def add_github_to_known_hosts():
    known_hosts_file = '/path/to/your/known_hosts/file'  # Specify the path to your known_hosts file
    
    # Execute the ssh-keyscan command
    process = subprocess.run(['ssh-keyscan', '-t', 'rsa', 'github.com'], capture_output=True, text=True)
    
    if process.returncode == 0:
        # Append the scanned host key to the known_hosts file
        with open(known_hosts_file, 'a') as f:
            f.write(process.stdout)
        print("GitHub has been added to known_hosts.")
    else:
        print("Failed to scan GitHub host key.")


def git_push(request):
    # Change to the root directory of your Django project
    root_directory = os.getcwd()
    git_directory = os.path.join(root_directory, '.git')
    headers = {'Authorization': f'token {github_token}'}
    #response = requests.get('https://api.github.com/path/to/api', headers=headers)

    if os.path.isdir(git_directory):
        print(f".git directory exists.{git_directory}")
    else:
        print(f".git directory does not exist.{git_directory}")

    # Add all files to the Git repository
    subprocess.run(['git', '-C', root_directory, 'add', '-A'])
    print("1\n")

    # Commit the changes
    subprocess.run(['git', '-C', root_directory, 'commit', '-m', 'Automatic commit'])
    print("2\n")
    # Push the changes to the remote repository
    subprocess.run(['git', '-C', root_directory, 'config', 'user.name', "aberguecio"])
    print("3\n")
    subprocess.run(['git', '-C', root_directory, 'config', 'user.password', github_token])
    print("4\n")
    remote_url = f"git@github.com:{username}/Git-Pusher.git"
    #add_github_to_known_hosts()
    print("5\n")
    subprocess.run(['git', '-C', root_directory, 'remote', 'set-url', 'origin', remote_url])
    print("6\n")
    subprocess.run(['git', '-C', root_directory, 'push'])
    print("7\n")
    # Redirect to a success page or return a response
    return "last"


""" import requests
# Create your views here.
def fetch_push_events(request):
    # Make a GET request to the GitHub API
    response = requests.get('https://api.github.com/events')

    # Check the response status code
    if response.status_code == 200:
        # The request was successful
        push_events = response.json()
    else:
        # Handle the error case
        push_events = []

    # Pass the push events to the template
    return render(request, 'push_events.html', {'push_events': push_events})
 """
