from django.test import TestCase
from stats_app.serializers import GithubUserSerializer


class GetDataTestCase(TestCase):

    def setup(self):
        token = ""

    def test_request(self):
        # todo get data make model objects save them
        print("hello world")


class SerializerTestCase(TestCase):

    def test_print_serializer(self):
        serializer = GithubUserSerializer()
        print(repr(serializer))
