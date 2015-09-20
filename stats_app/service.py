import requests
from urllib.parse import urljoin
import pandas as pd

GITHUB_API = 'https://api.github.com/'


def get_repository_list(username):
    req = requests.get(urljoin(GITHUB_API + 'users/', str(username) + '/repos'))
    repos_json = req.json()
    print(repos_json)
    repo_dict = [{'username': username, 'repo': repo["name"], 'created_at': repo["created_at"]} for repo in repos_json]
    print(repo_dict)
    return repo_dict


def get_repository_list_w_token(username, token): #todo figure out what this can help with and how to get it working
    headers = {'Authorization': 'token %s' % token}
    params = {'page': 2, 'per_page': 100}
    req_auth = requests.get(urljoin(GITHUB_API + 'users/', str(username) + '/repos'), headers=headers, params=params)
    repos_json = req_auth.json()
    repos = [{'username': username, 'repo': repo["name"]} for repo in repos_json]
    return repos


def get_commit_list(repo_dict):
    commits = []
    for repo in repo_dict:
        endpoint = GITHUB_API + 'repos/' + str(repo['username']) + '/' + str(repo['repo']) + '/commits'
        req_commit = requests.get(endpoint)
        commits_json = req_commit.json()
        d = [{'repo': repo['repo'], 'message': commit["commit"]["message"], 'date_effective': commit["commit"]["author"]["date"]} for commit in commits_json]
        commits.append(d)
    return commits


def get_commit_df(repo_dict):
    commits = pd.DataFrame()
    for repo in repo_dict:
        endpoint = GITHUB_API + 'repos/' + str(repo['username']) + '/' + str(repo['repo']) + '/commits'
        req_commit = requests.get(endpoint)
        commits_json = req_commit.json()
        d = [{'repo': repo['repo'], 'repo_created_date': repo['created_at'], 'message': commit["commit"]["message"], 'date_effective': commit["commit"]["author"]["date"]} for commit in commits_json]
        df = pd.DataFrame(d)
        commits = commits.append(df)
    return commits


def reshape_commit_data(df):
    df['date'] = pd.to_datetime(df['date_effective'])
    df_pivot = pd.pivot_table(data=df, index='date', columns='repo', aggfunc='count', values='message', fill_value=0)
    df_date = df_pivot.resample('w', how='sum', axis=0)
    df_date = df_date.fillna(0)
    return df_date.to_json(date_format='iso')




# json.dumps(list())











