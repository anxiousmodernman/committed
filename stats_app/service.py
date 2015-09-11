# from stats_app.serializers import GithubUserSerializer
# from django.utils.six import BytesIO
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import sys
# import argparse


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







