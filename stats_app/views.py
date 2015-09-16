from django.http import HttpResponse
from social.apps.django_app.default.models import UserSocialAuth
from stats_app.service import get_repository_list, get_commit_list


def stats(request):
    if request.method == 'GET':
        instance = UserSocialAuth.objects.get(user=request.user, provider='github')
        username = instance.extra_data['login']
        token = instance.access_token # todo DO WE NEED?
        repos = get_repository_list(username)
        commits = get_commit_list(repos)
        return HttpResponse(commits)



