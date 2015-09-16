from rest_framework import serializers
from stats_app.models import GithubUser, Repository, Commit


class GithubUserSerializer(serializers.ModelSerializer):
    repos = serializers.StringRelatedField(many=True)

    class Meta:
        model = GithubUser
        fields = ('username', 'repos') # todo, think about how we want to store this information


class RepositorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = ('name', 'description')


class CommitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commit
        fields = ('name', 'description', 'created_at')