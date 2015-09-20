from django.http import HttpResponse
from django.shortcuts import render
from social.apps.django_app.default.models import UserSocialAuth
import json
import pandas as pd

from stats_app.service import get_repository_list, reshape_commit_data, get_commit_df

TEST = True


def stats(request):
    if request.method == 'GET':
        instance = UserSocialAuth.objects.get(user=request.user, provider='github')
        username = instance.extra_data['login']
        token = instance.access_token  # todo DO WE NEED?
        if TEST:
            with open('stats_app/commit_pivot.json') as json_data:
                d = json.load(json_data)
            return HttpResponse(d)
        # if TEST_CSV:
        #     d = pd.read_csv('commit_pivot.csv')
        #     return HttpResponse(d)
        else:
            repos = get_repository_list(username)
            commits = get_commit_df(repos)
            commit_json = reshape_commit_data(commits)
            return HttpResponse(commit_json) #todo figure out datetime in json


def graph(request):
    return render(request, "stats_app/graph.html")





