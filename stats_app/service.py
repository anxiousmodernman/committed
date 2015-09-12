from stats_app.serializers import GithubUserSerializer, RepositorySerializer
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import sys
import argparse


import requests
import getpass
import json
from urllib.parse import urljoin


GITHUB_API = 'https://api.github.com/'


def get_user_token():
    username = input('Github username: ')
    password = getpass.getpass('Github password: ')
    note = input('Note (optional): ')
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}
    if note:
        payload['note'] = note
    res = requests.post(
        url,
        auth=(username, password),
        data = json.dumps(payload),
        )
    j = json.loads(res.text)
    if res.status_code >= 400:
        msg = j.get('message', 'UNDEFINED ERROR (no error description from server)')
        print('ERROR: %s' % msg)
        return
    token = j['token']
    print('New token: %s' % token)


def githubuser_to_model(json):
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = GithubUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        sys.exit("serialization failed!")


def githubrepository_to_model(json):
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = RepositorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        sys.exit("serialization failed!")

#todo GIVE DICT LIKE RESPONSES TO sqlitedb via MODELS, SERIALIZE


def get_repository_list(username):
    req = requests.get(urljoin(GITHUB_API + 'users/', str(username) + '/repos')) # todo, just use + ?
    repos_json = req.json()
    repo_dict = [{'username': username, 'repo': repo["name"]} for repo in repos_json]
    print(repo_dict)
    return repo_dict


def get_commit_list(repo_dict):
    commit_dict = []
    for repo in repo_dict:
        new_url = GITHUB_API + 'repos/' + str(repo['username']) + '/' + str(repo['repo']) + '/commits'
        print(new_url)
        req_commit = requests.get(new_url)
        commits = req_commit.json()
        print(commits[0])
        d = [{'repo': repo, 'message': commit["commit"]["message"], 'date_effective': commit["commit"]["author"]["date"]} for commit in commits]
        commit_dict.append(d)
    return commit_dict














