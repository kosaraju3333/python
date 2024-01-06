import requests
from flask import Flask

#Creating a flask app instance
app = Flask(__name__)

#Decorators
@app.route("/repos")
def spontan_repos_list():
    git_url = "https://api.github.com/orgs/spontansolutions/repos"
    response = requests.get(git_url)
    repo_lists = response.json()

    repos_name_list = []
    for repos in repo_lists:
        repo_name = repos["name"]
        repos_name_list.append(repo_name)
    return repos_name_list

spontan_repos_list()

#Flask Comes with Inbuild Server
app.run('0.0.0.0', port=3000)