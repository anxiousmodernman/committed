from django.test import TestCase
from stats_app.serializers import GithubUserSerializer, RepositorySerializer
from stats_app.service import get_repository_list, get_user_token, get_commit_df
from social.apps.django_app.default.models import UserSocialAuth


class GetTokenTestCase(TestCase):

    def test_get_user_token(self):
        get_user_token()


class GetDataTestCase(TestCase):

    def setup(self):
        token = ""

    def test_get_repos_list(self):
        repo_list = get_repository_list('ahelium')
        return repo_list

    def test_get_commit_list(self):
        repo_list = get_repository_list('ahelium')
        commit_df = get_commit_df(repo_list)
        print(commit_df)


class GetSocialAuthUserTestCase(TestCase):

    def test_get_user_fields(self):
        user = UserSocialAuth.objects.get(pk=1)
        token = user.extra_data['access_token']
        login = user.extra_data['login']
        print('user token:' + str(token) + 'user login:' + str(login))


class SerializerTestCase(TestCase):

    def test_print_user_serializer(self):
        serializer = GithubUserSerializer()
        print(repr(serializer))

    def test_print_repo_serializer(self):
        serializer = RepositorySerializer()
        print(repr(serializer))




