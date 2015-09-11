from django.test import TestCase
from stats_app.serializers import GithubUserSerializer
from stats_app.service import get_user_token


class GetDataTestCase(TestCase):

    def setup(self):
        token = ""

    def test_get_user_token(self):
        get_user_token()


class SerializerTestCase(TestCase):

    def test_print_serializer(self):
        serializer = GithubUserSerializer()
        print(repr(serializer))


