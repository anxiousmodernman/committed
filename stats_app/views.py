from django.http import HttpResponse
from django.shortcuts import render
from social.apps.django_app.default.models import UserSocialAuth
import json

from stats_app.service import get_repository_list, get_commit_list

TEST = True


def stats(request):
    if request.method == 'GET':
        instance = UserSocialAuth.objects.get(user=request.user, provider='github')
        username = instance.extra_data['login']
        token = instance.access_token  # todo DO WE NEED?
        if TEST:
            with open('stats_app/commits_clean.json') as json_data:
                d = json.load(json_data)
            return HttpResponse(d)
        else:
            repos = get_repository_list(username)
            commits = get_commit_list(repos)
            return HttpResponse(commits)


def graph(request):
    return render(request, "stats_app/graph.html")





