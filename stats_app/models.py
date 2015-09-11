from django.db import models


class GithubUser(models.Model):
    username = models.CharField(max_length=50)


class Repository(models.Model):
    name = models.CharField(max_length=100)
    githubuser = models.ForeignKey(GithubUser)


class Commit(models.Model):
    sha1hash = models.CharField(max_length=250)
    timestamp = models.DateTimeField()
    message = models.CharField(max_length=1000, null=True)
    repository = models.ForeignKey(Repository)

