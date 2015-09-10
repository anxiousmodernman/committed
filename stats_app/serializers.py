from rest_framework import serializers
from stats_app.models import GithubUser, Repository, Commit


class GithubUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = GithubUser

