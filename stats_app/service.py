import requests
from urllib.parse import urljoin


GITHUB_API = 'https://api.github.com/'


def get_repository_list(username):
    req = requests.get(urljoin(GITHUB_API + 'users/', str(username) + '/repos'))
    repos_json = req.json()
    print(repos_json)
    repo_dict = [{'username': username, 'repo': repo["name"]} for repo in repos_json]
    print(repo_dict)
    return repo_dict


def get_repository_list_w_token(username, token): #todo figure out what this can help with and how to get it working
    headers = {'Authorization': 'token %s' % token}
    params = {'page': 2, 'per_page': 100}
    req_auth = requests.get(urljoin(GITHUB_API + 'users/', str(username) + '/repos'), headers=headers, params=params)
    repos_json = req_auth.json()
    repo_dict = [{'username': username, 'repo': repo["name"]} for repo in repos_json]
    return repo_dict


def get_commit_list(repo_dict):
    commit_dict = []
    for repo in repo_dict:
        new_url = GITHUB_API + 'repos/' + str(repo['username']) + '/' + str(repo['repo']) + '/commits'
        req_commit = requests.get(new_url)
        commits = req_commit.json()
        d = [{'repo': repo['repo'], 'message': commit["commit"]["message"], 'date_effective': commit["commit"]["author"]["date"]} for commit in commits]
        commit_dict.append(d)
    return commit_dict












