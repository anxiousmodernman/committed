from django.db import models


class GithubUser(models.Model):
    username = models.CharField(max_length=50)


class Repository(models.Model):
    name = models.CharField(max_length=100)
    # todo foreign key to user


class Commit(models.Model):
    sha1hash = models.CharField(max_length=250)
    timestamp = models.DateTimeField()
    message = models.CharField(max_length=1000)
    repository = models.ForeignKey(Repository)
    # todo foreign key to repository


