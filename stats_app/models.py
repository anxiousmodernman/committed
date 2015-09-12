from django.db import models


#todo: REMOVE DEFAULT

class GithubUser(models.Model):
    username = models.CharField(max_length=50, default='ahelium')


class Repository(models.Model):
    githubuser = models.ForeignKey(GithubUser)
    name = models.CharField(max_length=100, default='rec-engine-sb')
    description = models.CharField(max_length=500, default='SB Rec Engine')



# class Commit(models.Model):
#     timestamp = models.DateTimeField()
#     message = models.CharField(max_length=1000, null=True)
#     repository = models.ForeignKey(Repository)

