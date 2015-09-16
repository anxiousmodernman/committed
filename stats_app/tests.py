from django.test import TestCase
from stats_app.serializers import GithubUserSerializer, RepositorySerializer
from stats_app.service import get_repository_list, get_user_token, get_commit_list
from stats_app.models import GithubUser


class GetTokenTestCase(TestCase):

    def test_get_user_token(self):
        get_user_token()


class GetDataTestCase(TestCase):

    def setup(self):
        token = ""

    # def test_get_repos_list(self):
    #     repo_list = get_repository_list('ahelium')
    #     return repo_list

    def test_get_commit_list(self):
        repo_list = get_repository_list('ahelium')
        print(get_commit_list(repo_list))


class GetUserTestCase(TestCase):

    def make_test_user(self):
        user = GithubUser(username='ahelium')
        user.save()

    def pull_user_information(self):
        print(GithubUser.objects.all())


class SerializerTestCase(TestCase):

    def test_print_user_serializer(self):
        serializer = GithubUserSerializer()
        print(repr(serializer))

    def test_print_repo_serializer(self):
        serializer = RepositorySerializer()
        print(repr(serializer))


