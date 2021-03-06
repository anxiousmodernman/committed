from rest_framework import serializers
from stats_app.models import Repository, Commit


class RepositorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = ('name', 'description')


class CommitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commit
        fields = ('name', 'description', 'created_at')